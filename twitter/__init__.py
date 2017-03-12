"""init"""
from twitter.twitter import Twitter

def twitter(consumer_key, consumer_secret, access_token, access_token_secret):
    """return Twitter Class"""
    return Twitter(consumer_key, consumer_secret, access_token, access_token_secret)
