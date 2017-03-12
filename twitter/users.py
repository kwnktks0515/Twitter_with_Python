"""users"""
from twitter.core import UserData

class Users:
    """users"""
    def __init__(self, twitter):
        self.twitter = twitter
    def lookup(self, params):
        """Get users information"""
        url = "/".join(["users", "lookup"])
        result = self.twitter.get(url, params=params)
        result.data = [UserData(url, text) for text in result.texts]
        return result
    def profile_banner(self, params):
        """Not support"""
        params = None
        return params
    def search(self, params):
        """Search users"""
        url = "/".join(["users", "search"])
        result = self.twitter.get(url, params=params)
        result.data = [UserData(url, text) for text in result.texts]
        return result
    def show(self, params):
        """Equal lookup"""
        return self.lookup(params)
    def suggestions(self, params):
        """Not support"""
        pass
    def report_spam(self, params):
        """Not support"""
        pass
