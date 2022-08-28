from requests import RequestException, Session
from requests_oauthlib import OAuth1

from twhook._version import __version__
from twhook.errors import APIError, TwhookError

BASE_URL = "https://api.twitter.com/1.1/account_activity/all"


class Twhook:
    """
    Twitter Premium Account Activity API (AAA) wrapper.

    Reference:
    https://developer.twitter.com/en/docs/twitter-api/premium/account-activity-api
    """
    def __init__(
            self, env_name, bearer_token, api_key=None, api_key_secret=None,
            access_token=None, access_token_secret=None
    ):
        self.env_name = env_name

        self.bearer_token = bearer_token

        self.api_key = api_key
        self.api_key_secret = api_key_secret
        self.access_token = access_token
        self.access_token_secret = access_token_secret

        self._session = Session()
        self._session.headers.update({"User-Agent": f"Twhook/{__version__}"})

        self._webhook = None
        self._subscription = None

    def get_user_auth(self, access_token=None, access_token_secret=None):
        if not (self.api_key and self.api_key_secret):
            raise TwhookError("Missing API key or API key secret.")
        if not (access_token or access_token_secret):
            access_token = self.access_token
            access_token_secret = self.access_token_secret
        if not (access_token and access_token_secret):
            raise TwhookError("Missing access token or access token secret.")

        return OAuth1(
            self.api_key, self.api_key_secret, access_token, access_token_secret
        )

    def request(self, method, resource_path, data=None, auth=None):
        url = '/'.join((BASE_URL, self.env_name, resource_path))
        headers = None

        if auth is None:
            # app-only auth
            headers = {"Authorization": f"Bearer {self.bearer_token}"}

        try:
            response = self._session.request(
                method, url, data=data, headers=headers, auth=auth
            )
        except RequestException as e:
            raise TwhookError("Unable to process request.") from e

        if response.status_code == 200:
            return response.json()
        if response.status_code == 204:
            return "ok"

        raise APIError(response)

    @property
    def webhook(self):
        if self._webhook is None:
            from twhook.premium import Webhook
            self._webhook = Webhook(self)
        return self._webhook

    @property
    def subscription(self):
        if self._subscription is None:
            from twhook.premium import Subscription
            self._subscription = Subscription(self)
        return self._subscription
