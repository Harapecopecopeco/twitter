from twiiter_client import TwitterClient
from datetime import date
from pprint import pprint

today = date.today()

screen_name = "panicyusuke"
request_count = 5
client = TwitterClient(dt=today, screen_name=screen_name)

# Get Tweets by user ids
# query = client.get_tweets(count=request_count)
# pprint(query)

# Get Likes by users
query = client.get_likes_by_user(count=request_count)
pprint(query)
