"""friendships"""
from twitter.core import UserData
class Friendships:
    """friendships"""
    def __init__(self, twitter):
        self.twitter = twitter
    def incoming(self, params):
        """Hello"""
        url = "/".join(["friendships", "incoming"])
        result = self.twitter.get(url, params=params)
        result.data = result.texts["ids"]
        result.next_cursor = result.texts["next_cursor"]
        result.previous_cursor = result.texts["previous_cursor"]
        result.get_texts_array = None
        result.get_texts_tuple = None
        return result
    def lookup(self, params):
        """Hello"""
        url = "/".join(["friendships", "lookup"])
        result = self.twitter.get(url, params=params)
        result.data = result.texts
        return result
    def no_retweets(self, params):
        """Hello"""
        url = "/".join(["friendships", "no_retweets", "ids"])
        result = self.twitter.get(url, params=params)
        result.data = result.texts
        result.get_texts_array = None
        result.get_texts_tuple = None
        return result
    def outgoing(self, params):
        """Hello"""
        url = "/".join(["friendships", "outgoing"])
        result = self.twitter.get(url, params=params)
        result.data = result.texts["ids"]
        result.next_cursor = result.texts["next_cursor"]
        result.previous_cursor = result.texts["previous_cursor"]
        result.get_texts_array = None
        result.get_texts_tuple = None
        return result
    def show(self, params):
        """Hello"""
        url = "/".join(["friendships", "show"])
        result = self.twitter.get(url, params=params)
        result.data.append(result.texts["relationship"]["source"])
        result.data.append(result.texts["relationship"]["target"])
        return result
    def create(self, params):
        """Hello"""
        url = "/".join(["friendships", "create"])
        result = self.twitter.post(url, params=params)
        result.data = [UserData(url, result.texts)]
        return result
    def destroy(self, params):
        """Hello"""
        url = "/".join(["friendships", "destroy"])
        result = self.twitter.post(url, params=params)
        result.data = [UserData(url, result.texts)]
        return result
    def update(self, params):
        """Hello"""
        url = "/".join(["friendships", "update"])
        result = self.twitter.post(url, params=params)
        result.data = [UserData(url, result.texts)]
        return result
    