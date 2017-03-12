# coding: UTF-8
"""statuses"""
from twitter.core import TweetData

class Statuses:
    """statuses"""
    def __init__(self, twitter):
        self.twitter = twitter
    def home_timeline(self, params):
        """Get Home TimeLine"""
        url = "/".join(["statuses", "home_timeline"])
        result = self.twitter.get(url, params=params)
        result.data = [TweetData(url, text) for text in result.texts]
        return result
    def lookup(self, params):
        """Get Tweets"""
        url = "/".join(["statuses", "lookup"])
        result = self.twitter.get(url, params=params)
        result.data = [TweetData(url, text) for text in result.texts]
        return result
    def mentions_timeline(self, params):
        """Get Mention TimeLine"""
        url = "/".join(["statuses", "mentions_timeline"])
        result = self.twitter.get(url, params=params)
        result.data = [TweetData(url, text) for text in result.texts]
        return result
    def oembed(self):
        """Not support"""
        pass
    def retweeters(self, params):
        """Hello"""
        url = "/".join(["statuses", "retweeters", "ids"])
        result = self.twitter.get(url, params=params)
        result.data = result.texts["ids"]
        result.next_cursor = result.texts["next_cursor"]
        result.previous_cursor = result.texts["previous_cursor"]
        result.get_texts_array = None
        result.get_texts_tuple = None
        return result
    def retweets(self, tweet_id, params):
        """Hello"""
        url = "/".join(["statuses", "retweets", str(tweet_id)])
        result = self.twitter.get(url, params=params)
        result.data = [TweetData(url, text) for text in result.texts]
        return result
    def retweets_of_me(self, params):
        """Hello"""
        url = "/".join(["statuses", "retweets_of_me"])
        result = self.twitter.get(url, params=params)
        result.data = [TweetData(url, text) for text in result.texts]
        return result
    def show(self, params):
        """Hello"""
        url = "/".join(["statuses", "show"])
        result = self.twitter.get(url, params=params)
        result.data = [TweetData(url, result.texts)]
        return result
    def user_timeline(self, params):
        """Hello"""
        url = "/".join(["statuses", "user_timeline"])
        result = self.twitter.get(url, params=params)
        result.data = [TweetData(url, text) for text in result.texts]
        return result
    def destroy(self, tweet_id, params):
        """Hello"""
        url = "/".join(["statuses", "destroy", str(tweet_id)])
        result = self.twitter.post(url, params=params)
        result.data = [TweetData(url, result.texts)]
        return result
    def retweet(self, tweet_id, params):
        """Hello"""
        url = "/".join(["statuses", "retweet", str(tweet_id)])
        result = self.twitter.post(url, params=params)
        result.data = [TweetData(url, result.texts)]
        return result
    def unretweet(self, tweet_id, params):
        """Hello"""
        url = "/".join(["statuses", "unretweet", str(tweet_id)])
        result = self.twitter.post(url, params=params)
        result.data = [TweetData(url, result.texts)]
        return result
    def update(self, params):
        """Hello"""
        url = "/".join(["statuses", "update"])
        result = self.twitter.post(url, params=params)
        result.data = [TweetData(url, result.texts)]
        return result
