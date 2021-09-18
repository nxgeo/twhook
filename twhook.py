from typing import Union

from requests import request
from requests_oauthlib import OAuth1, OAuth2


class TwhookError(Exception):
    pass


class Twhook:
    """
    Twitter Premium Account Activity API (AAA) wrapper
    that helps you to manage webhooks and subscriptions.

    Reference:
    https://developer.twitter.com/en/docs/twitter-api/premium/account-activity-api/
    """
    BASE_URL = 'https://api.twitter.com/1.1/account_activity/all/'

    def __init__(
            self,
            consumer_key: str,
            consumer_secret: str,
            access_token: str,
            access_token_secret: str,
            bearer_token: str,
            env_name: str
    ) -> None:
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret

        self.env_name = env_name

        self._user_context_auth = OAuth1(
            self.consumer_key, self.consumer_secret,
            access_token, access_token_secret
        )

        self._app_only_auth = OAuth2(
            token={'access_token': bearer_token}
        )

    def _request(
            self, method, endpoint, with_env=True,
            data=None, auth=None
    ):
        if with_env:
            endpoint = f'{self.env_name}/{endpoint}'

        response = request(
            method, Twhook.BASE_URL+endpoint, data=data,
            auth=(auth or self._app_only_auth)
        )

        if response.status_code not in [200, 204]:
            raise TwhookError(response.json())

        if response.status_code == 204:
            return True

        return response.json()

    def register(self, url: str) -> dict:
        """Registers a webhook URL."""
        return self._request(
            'POST', 'webhooks.json', data={'url': url},
            auth=self._user_context_auth
        )

    def trigger_crc(self, webhook_id: str) -> bool:
        """Manually triggers a challenge-response check."""
        return self._request('PUT', f'webhooks/{webhook_id}.json')

    def get_webhooks(self, with_env: bool = False) -> Union[dict, list]:
        """Returns all webhook URLs and their statuses."""
        return self._request('GET', 'webhooks.json', with_env)

    def delete(self, webhook_id: str) -> bool:
        """Deletes the webhook."""
        return self._request('DELETE', f'webhooks/{webhook_id}.json')

    def _subscription(
            self, method: str,
            token: str = None, secret: str = None
    ) -> bool:
        """Handling methods subscribe() and is_subscribed()."""
        if (token and not secret) or (not token and secret):
            raise TwhookError('Incomplete credentials.')

        if token and secret:
            auth = OAuth1(
                self.consumer_key, self.consumer_secret,
                token, secret
            )
        else:
            auth = self._user_context_auth

        return self._request(method, 'subscriptions.json', auth=auth)

    def subscribe(self, **kwargs) -> bool:
        """Subscribes an application to an account's events."""
        return self._subscription('POST', **kwargs)

    def is_subscribed(self, **kwargs) -> bool:
        """Check to see if a webhook subscribed to an account."""
        return self._subscription('GET', **kwargs)

    def get_subscriptions_count(self) -> dict:
        """Returns a count of currently active subscriptions."""
        return self._request('GET', 'subscriptions/count.json', False)

    def get_subscriptions_list(self) -> dict:
        """Returns a list of currently active subscriptions."""
        return self._request('GET', 'subscriptions/list.json')

    def unsubscribe(self, user_id: str) -> bool:
        """Deactivates a subscription."""
        return self._request('DELETE', f'subscriptions/{user_id}.json')
