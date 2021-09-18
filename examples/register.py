from twhook import Twhook, TwhookError

CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_TOKEN = ''
ACCESS_TOKEN_SECRET = ''
BEARER_TOKEN = ''

ENV_NAME = ''

twh = Twhook(
    CONSUMER_KEY, CONSUMER_SECRET,
    ACCESS_TOKEN, ACCESS_TOKEN_SECRET,
    BEARER_TOKEN, ENV_NAME
)

url = ''

try:
    r = twh.register(url)
except TwhookError as e:
    print(e)
else:
    print(r)
