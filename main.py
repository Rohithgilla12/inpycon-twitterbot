"""
Script for execution of the bot
"""
import time  # for giving 15 seconds break between tweets
import tweepy  # for twitter API
from django.utils.encoding import smart_str
twitter = "https://twitter.com"


class Tweet:
    def __init__(self, consumer_key, consumer_secret, access_token, access_token_secret, search_terms):
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret
        self.access_token = access_token
        self.access_token_secret = access_token_secret
        self.search_terms = search_terms

    def auth(self):
        auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
        auth.set_access_token(self.access_token, self.access_token_secret)
        api = tweepy.API(auth)
        return api

    def run(self):
        while True:
            for search_term in self.search_terms:
                for tweet in tweepy.Cursor(self.auth().search, q=search_term).items(10):
                    if self.auth().get_status(tweet.id):
                        pass
                    else:
                        self.follow_them(tweet)
                        self.tweet_and_like(tweet)
                        try:
                            if smart_str(tweet.author.screen_name) != self.auth().me().screen_name:
                                self.auth().update_status(self.get_perfect(tweet))
                                print("Re tweeted with comment of -" + tweet.author.screen_name)
                        except tweepy.TweepError:
                            pass  # Already re tweeted
            time.sleep(20)

    @staticmethod
    def tweet_and_like(self, tweet):
        try:
            tweet.retweet()
            tweet.favorite()
        except tweepy.TweepError:
            pass  # Already re tweeted and liked

    def follow_them(self, tweet):
        try:
            self.auth().create_friendship(tweet.id)
        except tweepy.TweepError:
            pass  # Already a friend

    @staticmethod
    def get_perfect(self, tweet):
        url = twitter + "/" + tweet.author.screen_name + \
              "/" + "status" + "/" + str(tweet.id)
        perfect = smart_str("#PyConIndia2018" + " " +
                            "#pyconindia" + " " +
                            "#PyConIndia \n" + url)
        return perfect


Tweet("Consumer Key",
      "Consumer Secret",
      "Access token",
      "Access_token_secret", ["#PyConIndia2018", "#PyConIndia", "@pyconindia", "pyconindia"]).run()
