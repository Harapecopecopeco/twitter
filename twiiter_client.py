import os

from pprint import pprint

from twitter import Twitter, OAuth
from dotenv import load_dotenv

load_dotenv(verbose=True)

client = Twitter(
    auth=OAuth(
        token=os.getenv("ACCESS_TOKEN"),
        token_secret=os.getenv("ACCESS_TOKEN_SECRET"),
        consumer_key=os.getenv("CONSUMER_KEY"),
        consumer_secret=os.getenv("CONSUMER_SECRET_KEY")
    )
)

class TwitterClient:

    @classmethod
    def get_follower(cls, count:int, base_id:str):
    """ Get
    """
