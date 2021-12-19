import os
import sys

from datetime import date
from requests_oauthlib import OAuth1
import urllib
import dataclasses

import requests
from dotenv import load_dotenv

from error.query import TwitterApiV2Error, ResourceNotFound, GenericProblem

from oauthlib.oauth2 import WebApplicationClient

load_dotenv(verbose=True)


@dataclasses.dataclass
class TwitterClient:
    screen_name: str
    dt: date
    base_url = "https://api.twitter.com/2"
    user_id = None

    def __post_init__(self):
        self.auth = OAuth1(
            client_key=os.getenv("CONSUMER_KEY"),
            client_secret=os.getenv("CONSUMER_SECRET_KEY"),
            resource_owner_key=os.getenv("ACCESS_TOKEN"),
            resource_owner_secret=os.getenv("ACCESS_TOKEN_SECRET")
        )
        convert_username_to_userid_url = f"{self.base_url}/users/by/username/{self.screen_name}"
        try:
            users = requests.get(url=convert_username_to_userid_url, auth=self.auth)
            error_handle = users.json().get("errors")
            if error_handle:
                error_handle = error_handle[0].get("type")
                TwitterApiV2Error(url=error_handle)
            else:
                print("Success, No Error")
                self.user_id = users.json()["data"]["id"]
        except ResourceNotFound as RNF:
            pass
        except ConnectionError:
            print("connection error")
        else:
            print("ok")

    def info(self, *args):
        r""" Search User Information

        Args:
            # user_id (int): Target user id for retrieving user information.
            *args (list): []

        Returns:
            user_info (dict): user data scheme.

        References:
            Twitter API v2 Document:
            - https://developer.twitter.com/en/docs/twitter-api/users/lookup/api-reference/get-users-id
        """
        request_fields = {
            "id": True, "description": True,
        }

        # Parse dict(json) to request string
        request = ",".join([k for k, v in request_fields.items() if v])
        if self.user_id:
            url = f"{self.base_url}/users/{self.user_id}?user.fields={request}"
            return requests.get(url=url, auth=self.auth).json()
        else:
            return "Error: Could not find the user. Make sure that your screen name is correct."

    def follower_list(self, count):
        r""" Retrieve Follower List

        Args:
            # user_id (int): Target user id for retrieving user information.
            count (int): Search Limit Count for API Call Limit.

        Returns:
            follower list (dict): follower data list.

        References:
            Twitter API v2 Document:
            - https://developer.twitter.com/en/docs/twitter-api/users/lookup/api-reference/get-users-id
        """
        # Parse dict(json) to request string
        if self.user_id:
            url = f"{self.base_url}/users/{self.user_id}/followers?max_results={count}"
            return requests.get(url=url, auth=self.auth).json()
        else:
            return "Error: Could not find the user. Make sure that your screen name is correct."

    def search_keyword(self, keyword: str, count: int):
        r""" For SHOKUPAN

        Args:
            # user_id (int): Target user id for retrieving user information.
            keyword (str): Search word.
            count (int): Search Limit Count for API Call Limit.

        Returns:
            Tweet Object (dict): TBD.

        References:
            Twitter API v2 Document:
            - https://developer.twitter.com/en/docs/twitter-api/users/lookup/api-reference/get-users-id
        """

        if self.user_id:
            url = f"{self.base_url}/tweets/search/recent?query={keyword}"
            return requests.get(url=url, auth=self.auth).json()
        else:
            return ""

    def get_tweets(self, count: int):
        r""" Retrieve Tweets Object by user ids

        Args:
            count (int): API Call Limits.

        Returns:
            Tweet Object (dict): TBD.

        References:
            Twitter API v2 Document:
            - https://developer.twitter.com/en/docs/twitter-api/users/lookup/api-reference/get-users-id
        """

        if self.user_id:
            url = f"{self.base_url}/users/{self.user_id}/tweets"
            return requests.get(url=url, auth=self.auth).json()
        else:
            return ""

    def get_likes_by_user(self, count: int):
        r""" Retrieve Likes Object by user id

        Args:
            count (int): API Call Limits.

        Returns:
            Tweet Object (dict): TBD.

        References:
            Twitter API v2 Document:
            - https://developer.twitter.com/en/docs/twitter-api/users/lookup/api-reference/get-users-id
        """

        if self.user_id:
            max_result = f"max_results={count}"
            query_options = f"&tweet.fields=created_at"

            url = f"{self.base_url}/users/{self.user_id}/liked_tweets?"
            response = requests.get(
                url=url + max_result + query_options,
                auth=self.auth
            ).json().get("data")
            if response:
                return [{
                    "created_at": data.get("created_at"),
                    "tweet_id": data.get("id"),
                    "text": data.get("text")
                } for data in response]
            else:
                return {"data": "Nothing"}

    def get_timeline(self, count: int):
        r""" Retrieve Tweets Object by user ids

        Args:
            count (int): API Call Limits.

        Returns:
            Tweet Object (dict): TBD.

        References:
            Twitter API v2 Document:
            - https://developer.twitter.com/en/docs/twitter-api/users/lookup/api-reference/get-users-id
        """

        if self.user_id:
            url = f"{self.base_url}/users/{self.user_id}/tweets"
            response = requests.get(url=url, auth=self.auth).json().get("data")
            if response:
                return [{
                    "created_at": response.get("created_at")
                } for data in response]
            else:
                return {"data": "Nothing"}
        else:
            return ""
