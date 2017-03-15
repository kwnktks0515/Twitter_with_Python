"""Application"""

class Application:
    """Application"""
    def __init__(self, twitter):
        self.twitter = twitter
    def rate_limit_status(self, params):
        """H"""
        url = "/".join(["application", "rate_limit_status"])
        result = self.twitter.get(url, params=params)
        result.data = result.texts["resources"]
        return result
