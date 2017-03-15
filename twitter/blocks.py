"""blocks"""
from twitter.core import UserData

class Blocks:
    """blocks"""
    def __init__(self, twitter):
        self.twitter = twitter
    def ids(self, params):
        """Hello"""
        url = "/".join(["blocks", "ids"])
        result = self.twitter.get(url, params=params)
        result.data = result.texts["ids"]
        result.next_cursor = result.texts["next_cursor"]
        result.previous_cursor = result.texts["previous_cursor"]
        return result
    def list(self, params):
        """Hello"""
        url = "/".join(["blocks", "list"])
        result = self.twitter.get(url, params=params)
        result.data = [UserData(url, text) for text in result.texts["users"]]
        result.next_cursor = result.texts["next_cursor"]
        result.previous_cursor = result.texts["previous_cursor"]
        return result
    def create(self, params):
        """Hello"""
        url = "/".join(["blocks", "create"])
        result = self.twitter.post(url, params=params)
        result.data = [UserData(url, result.texts)]
        return result
    def destroy(self, params):
        """Hello"""
        url = "/".join(["blocks", "destroy"])
        result = self.twitter.post(url, params=params)
        result.data = [UserData(url, result.texts)]
        return result
