"""favorites"""
from twitter.core import TweetData

class Favorites:
    """favorites"""
    def __init__(self, twitter):
        self.twitter = twitter
    def list(self, params):
        """Hello"""
        url = "/".join(["favorites", "list"])
        result = self.twitter.get(url, params=params)
        result.data = [TweetData(url, text) for text in result.texts]
        return result
    def create(self, params):
        """Hello"""
        url = "/".join(["favorites", "create"])
        result = self.twitter.post(url, params=params)
        result.data = [TweetData(url, result.texts)]
        return result
    def destroy(self, params):
        """Hello"""
        url = "/".join(["favorites", "destroy"])
        result = self.twitter.post(url, params=params)
        result.data = [TweetData(url, result.texts)]
        return result
