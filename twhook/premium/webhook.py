class Webhook:
    def __init__(self, twhook):
        self._twhook = twhook

    def register(self, webhook_url):
        user_auth = self._twhook.get_user_auth()
        data = {"url": webhook_url}
        return self._twhook.request("POST", "webhooks.json", data, user_auth)

    def list(self, *, list_all=False):
        resource = "webhooks.json"
        if list_all:
            # skip env_name
            resource = f"../{resource}"
        return self._twhook.request("GET", resource)

    def validate(self, webhook_id):
        return self._twhook.request("PUT", f"webhooks/{webhook_id}.json")

    def delete(self, webhook_id):
        return self._twhook.request("DELETE", f"webhooks/{webhook_id}.json")
