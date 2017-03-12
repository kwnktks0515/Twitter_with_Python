"""saved_searches"""
from twitter.core import SavedSearchData
class SavedSearches:
    """saved_searches"""
    def __init__(self, twitter):
        self.twitter = twitter
    def list(self):
        """Hello"""
        url = "/".join(["saved_searches", "list"])
        result = self.twitter.get(url, params=None)
        result.data = [SavedSearchData(url, text) for text in result.texts]
        return result
    def show(self, _id):
        """Hello"""
        url = "/".join(["saved_searches", "show", str(_id)])
        result = self.twitter.get(url, params=None)
        result.data = [SavedSearchData(url, result.texts)]
        return result
    def create(self, params):
        """Hello"""
        url = "/".join(["saved_searches", "create"])
        result = self.twitter.post(url, params=params)
        result.data = [SavedSearchData(url, result.texts)]
        return result
    def destroy(self, _id):
        """Hello"""
        url = "/".join(["saved_searches", "destroy", str(_id)])
        result = self.twitter.post(url, params=None)
        result.data = [SavedSearchData(url, result.texts)]
        return result
