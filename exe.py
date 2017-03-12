"""Use Twitter"""

from twitter import twitter

if __name__ == "__main__":
    TWITTER = twitter(
        consumer_key="xx",
        consumer_secret="xx",
        access_token="xx",
        access_token_secret="xx"
    )

    # ----- application ----- Bat
    #TWITTER.rate_limit_status({})
