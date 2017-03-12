"""Search"""
from twitter.core import TweetData

class Search:
    """Search"""
    def __init__(self, twitter):
        self.twitter = twitter
    def tweets(self, params):
        """
        search tweets
        """
        url = "/".join(["search", "tweets"])
        result = self.twitter.get(url, params=params)
        result.data = [TweetData(url, text) for text in result.texts["statuses"]]
        result.search_metadata = result.texts["search_metadata"]
        return result
