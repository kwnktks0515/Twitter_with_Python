"""Twitter class"""

# oauth:http://docs.python-requests.org/en/master/

#import json
from twitter.statuses import Statuses
from twitter.account import Account
from twitter.users import Users
from twitter.trends import Trends
from twitter.search import Search
from twitter.saved_searches import SavedSearches
from twitter.mutes import Mutes
from twitter.friendships import Friendships
from twitter.friends import Friends
from twitter.followers import Followers
from twitter.favorites import Favorites
from requests_oauthlib import OAuth1Session

class Twitter:
    """Twitter class"""
    def __init__(self, consumer_key, consumer_secret, access_token, access_token_secret):
        self.twitter = OAuth1Session(consumer_key, consumer_secret, access_token, access_token_secret)
        self.core = Core(self.twitter)
        self.statuses = Statuses(self.core)
        self.account = Account(self.core)
        self.users = Users(self.core)
        self.trends = Trends(self.core)
        self.search = Search(self.core)
        self.saved_searches = SavedSearches(self.core)
        self.mutes = Mutes(self.core)
        self.friendships = Friendships(self.core)
        self.friends = Friends(self.core)
        self.followers = Followers(self.core)
        self.favorites = Favorites(self.core)

    def search_tweets(self):
        """Hello"""
        pass

SETTING = 0
class Core:
    """minimum"""
    def __init__(self, twitter):
        self._twitter = twitter
    def get(self, url, params):
        """
        Get request Twitter Server
        Return Data Class
        """
        return Data(url, self._twitter.get("https://api.twitter.com/1.1/"+url+".json", params=params))
    def post(self, url, params):
        """
        POST request Twitter Server
        Return Data Class
        """
        return Data(url, self._twitter.post("https://api.twitter.com/1.1/"+url+".json", params=params))

class Data:
    """H"""
    def __init__(self, name, texts):
        self.name = name
        self.status_code = texts.status_code
        self.headers = texts.headers
        self.encodeing = texts.encoding
        self.texts = texts.json()
        self.data = []

    def get_header(self, *words):
        """H"""
        if len(words) == 0:
            return self.headers
        else:
            return [self.headers[word] for word in words]

    def get_texts_array(self, *words):
        """H"""
        if len(words) == 0:
            return [func.get_texts(words) for func in self.data]
        else:
            if SETTING == 0:
                return [list(user) for user in zip(*[func.get_texts(words) for func in self.data])]
            else:
                return [func.get_texts(words) for func in self.data]

    def get_texts_tuple(self, *words):
        """H"""
        if len(words) == 0:
            return [func.get_texts(words) for func in self.data]
        else:
            if SETTING == 0:
                return tuple([list(user) for user in zip(*[func.get_texts(words) for func in self.data])])
            else:
                return tuple(func.get_texts(words) for func in self.data)
