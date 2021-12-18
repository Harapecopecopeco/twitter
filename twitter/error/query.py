"""Example Google style docstrings.

This error class manages the query execution errors in TwitterAPI v2.
The Twitter API does not hold errors as numbers, such as status codes, but as url_type.

"""
import sys
from .errors import query_errors


class TwitterApiV2Error(Exception):
    message: str
    class_name: str
    function_name: str
    line_number: int
    errors = query_errors

    def __init__(self, url):
        self.type_url = url
        self.error_handle()

    def error_handle(self):
        if self.type_url == "https://api.twitter.com/2/problems/resource-not-found":
            print("Raise ResourceNotFound")
            raise ResourceNotFound


class GenericProblem(TwitterApiV2Error):

    def __init__(self, message):
        super().__init__(f"{self.message}\ncf. {self.type_url}")


class ResourceNotFound(TwitterApiV2Error):

    def __init__(self):
        self.message = self.errors.get("type_url")
        super().__init__(f"{self.message}")
        print(f"ResourceNotFound class name: {type(self).__name__}")
        err_info = self.errors.get(self.__class__.__name__)
        self.class_name = self.__class__.__name__
        self.function_name = sys._getframe().f_code.co_name
        self.line_number = sys._getframe().f_lineno
        error_place = f"Class: {self.class_name}, Function: {self.function_name}, Line number: {self.line_number}"
        print(error_place)
