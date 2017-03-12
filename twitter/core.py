"""minimum"""
SETTING = 0

class Minimum:
    """H"""
    def __init__(self, name, texts):
        self.name = name
        self.texts = texts
    def get_texts(self, words):
        """Hello"""
        if len(words) == 0:
            return self.texts
        else:
            return [self.texts[word] for word in words]

class TweetData(Minimum):
    """Date"""
class UserData(Minimum):
    """H"""
class TrendData(Minimum):
    """H"""
class SavedSearchData(Minimum):
    """H"""
class PlaceData(Minimum):
    """H"""
class EntityData(Minimum):
    """H"""
class ListData(Minimum):
    """H"""
