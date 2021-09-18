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

try:
    r = twh.subscribe()
    # r = twh.subscribe(token='', secret='')
except TwhookError as e:
    print(e)
else:
    print(r)
