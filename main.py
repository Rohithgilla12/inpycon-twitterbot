"""
Main script file for execution of the bot
"""
import time  # for giving 15 seconds break between tweets
import tweepy  # for twitter API
from django.utils.encoding import smart_str


# Twitter Access Tokens

from config import consumer_key
from config import consumer_secret
from config import access_token
from config import access_token_secret
from config import searchterms
from config import volunteertwitterhandle

# Connecting to twitter service

AUTH = tweepy.OAuthHandler(consumer_key, consumer_secret)
AUTH.set_access_token(access_token, access_token_secret)
API = tweepy.API(AUTH)

TWEETS = []  # For collection of all tweets it acts as db for tweets
NAMES = []   # For collection of all user ids it acts as db for userids

while True:
    for searchterm in searchterms:
        for tweet in tweepy.Cursor(API.search, q=searchterm).items(10):
            if tweet in TWEETS:
                pass
            else:
                TWEETS.append(tweet.text)
                if tweet.author.id not in NAMES:
                    NAMES.append(tweet.author.id)
                try:
                    tweet.retweet()
                    if smart_str(tweet.author.screen_name) != volunteertwitterhandle:
                        perfect = "RT @" + \
                                  smart_str(tweet.author.screen_name) + \
                                  " "+smart_str(tweet.text)
                        API.update_status(perfect)
                        print("Retweeted")
                except tweepy.TweepError:
                    pass
    for i in NAMES:
        try:
            API.create_friendship(i)
            # Following the person who tweeted with #PyConIndia #PyConIndia2018
        except tweepy.TweepError:
            pass
    time.sleep(15)
