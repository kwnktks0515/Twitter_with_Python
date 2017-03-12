"""trends"""
from twitter.core import TrendData

class Trends:
    """trends"""
    def __init__(self, twitter):
        self.twitter = twitter
    def available(self):
        """Hello"""
        url = "/".join(["trends", "available"])
        result = self.twitter.get(url, params=None)
        result.data = result.texts
        result.get_texts_array = None
        result.get_texts_tuple = None
        return result
    def closest(self, params):
        """Hello"""
        url = "/".join(["trends", "closest"])
        result = self.twitter.get(url, params=params)
        result.data = result.texts
        result.get_texts_array = None
        result.get_texts_tuple = None
        return result
    def place(self, params):
        """Hello"""
        url = "/".join(["trends", "place"])
        result = self.twitter.get(url, params=params)
        result.texts = result.texts[0]
        result.data = [TrendData(url, text) for text in result.texts["trends"]]
        result.as_of = result.texts["as_of"]
        result.created_at = result.texts["created_at"]
        result.locations = result.texts["locations"]
        return result
