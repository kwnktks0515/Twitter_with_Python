"""mutes"""
from twitter.core import UserData

class Mutes:
    """mutes"""
    def __init__(self, twitter):
        self.twitter = twitter
    def users_ids(self, params):
        """Hello"""
        url = "/".join(["mutes", "users", "ids"])
        result = self.twitter.get(url, params=params)
        result.data = result.texts["ids"]
        result.next_cursor = result.texts["next_cursor"]
        result.previous_cursor = result.texts["previous_cursor"]
        result.get_texts_array = None
        result.get_texts_tuple = None
        return result
    def users_list(self, params):
        """H"""
        url = "/".join(["mutes", "users", "list"])
        result = self.twitter.get(url, params=params)
        result.data = [UserData(url, text) for text in result.texts["users"]]
        result.next_cursor = result.texts["next_cursor"]
        result.previous_cursor = result.texts["previous_cursor"]
        return result
    def users_create(self, params):
        """H"""
        url = "/".join(["mutes", "users", "create"])
        result = self.twitter.post(url, params=params)
        result.data = [UserData(url, result.texts)]
        return result
    def users_destroy(self, params):
        """H"""
        url = "/".join(["mutes", "users", "destroy"])
        result = self.twitter.post(url, params=params)
        result.data = [UserData(url, result.texts)]
        return result
