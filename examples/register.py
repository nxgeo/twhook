from twhook import Twhook
from twhook.errors import TwhookError

ENV_NAME = ""

BEARER_TOKEN = ""

API_KEY = ""
API_KEY_SECRET = ""
ACCESS_TOKEN = ""
ACCESS_TOKEN_SECRET = ""

twhook = Twhook(
    ENV_NAME, BEARER_TOKEN,
    API_KEY, API_KEY_SECRET,
    ACCESS_TOKEN, ACCESS_TOKEN_SECRET
)

webhook_url = ""

try:
    response = twhook.webhook.register(webhook_url)
except TwhookError as e:
    print(e)
else:
    print(response)
