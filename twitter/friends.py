"""friends"""
from twitter.core import UserData

class Friends:
    """friends"""
    def __init__(self, twitter):
        self.twitter = twitter
    def ids(self, params):
        """Hello"""
        url = "/".join(["friends", "ids"])
        result = self.twitter.get(url, params=params)
        result.data = result.texts["ids"]
        result.next_cursor = result.texts["next_cursor"]
        result.previous_cursor = result.texts["previous_cursor"]
        result.get_texts_array = None
        result.get_texts_tuple = None
        return result
    def list(self, params):
        """Hello"""
        url = "/".join(["friends", "list"])
        result = self.twitter.get(url, params=params)
        result.data = [UserData(url, text) for text in result.texts["users"]]
        result.next_cursor = result.texts["next_cursor"]
        result.previous_cursor = result.texts["previous_cursor"]
        return result
