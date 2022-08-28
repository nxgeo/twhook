from requests.exceptions import JSONDecodeError


class TwhookError(Exception):
    pass


class APIError(TwhookError):
    def __init__(self, response):
        try:
            error = response.json()["errors"][0]
        except (JSONDecodeError, KeyError, IndexError):
            self.code = response.status_code
            self.message = response.reason
        else:
            self.code = error["code"]
            self.message = error["message"]

        super().__init__(f"[Error {self.code}] {self.message}")
