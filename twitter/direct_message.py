"""direct_messages"""
from twitter.core import DirectMessageData

class DirectMessages:
    """direct_messages"""
    def __init__(self, twitter):
        self.twitter = twitter
    def get(self, params):
        """Hello"""
        url = "direct_messages"
        result = self.twitter.get(url, params=params)
        result.data = [DirectMessageData(url, text) for text in result.texts]
        return result
    def sent(self, params):
        """Hello"""
        url = "/".join(["direct_messages", "sent"])
        result = self.twitter.get(url, params=params)
        result.data = [DirectMessageData(url, text) for text in result.texts]
        return result
    def show(self, params):
        """Hello"""
        url = "/".join(["direct_messages", "show"])
        result = self.twitter.get(url, params=params)
        result.data = [DirectMessageData(url, result.texts)]
        return result
    def destroy(self, params):
        """Hello"""
        url = "/".join(["direct_messages", "destroy"])
        result = self.twitter.post(url, params=params)
        result.data = [DirectMessageData(url, result.texts)]
        return result
    def new(self, params):
        """Hello"""
        url = "/".join(["direct_messages", "new"])
        result = self.twitter.post(url, params=params)
        result.data = [DirectMessageData(url, result.texts)]
        return result
