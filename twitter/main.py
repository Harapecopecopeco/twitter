from twiiter_client import TwitterClient
from datetime import date
from pprint import pprint

today = date.today()

screen_name = "shoku_pan_pan"
request_count = 5
client = TwitterClient(dt=today, screen_name=screen_name)

# Get Tweets by user ids
query = client.tweets(count=request_count)
pprint(query)
