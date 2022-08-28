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

# access_token = ""
# access_token_secret = ""

try:
    response = twhook.subscription.add()
    # response = twhook.subscription.add(access_token, access_token_secret)
except TwhookError as e:
    print(e)
else:
    print(response)
