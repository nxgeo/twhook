class Subscription:
    def __init__(self, twhook):
        self._twhook = twhook

    def add(self, access_token=None, access_token_secret=None):
        user_auth = self._twhook.get_user_auth(access_token, access_token_secret)
        return self._twhook.request("POST", "subscriptions.json", auth=user_auth)

    def check(self, access_token=None, access_token_secret=None):
        user_auth = self._twhook.get_user_auth(access_token, access_token_secret)
        return self._twhook.request("GET", "subscriptions.json", auth=user_auth)

    def count(self):
        return self._twhook.request("GET", "../subscriptions/count.json")

    def list(self):
        return self._twhook.request("GET", "subscriptions/list.json")

    def delete(self, user_id):
        return self._twhook.request("DELETE", f"subscriptions/{user_id}.json")
