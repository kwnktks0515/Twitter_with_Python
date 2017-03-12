"""friendships"""

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
        pass
    def no_retweets(self, params):
        """Hello"""
        pass
    def outgoing(self, params):
        """Hello"""
        pass
    def show(self, params):
        """Hello"""
        pass
    def create(self, params):
        """Hello"""
        pass
    def destroy(self, params):
        """Hello"""
        pass
    def update(self, params):
        """Hello"""
        pass
    