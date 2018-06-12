"""
Script for execution of the bot
"""
import time  # for giving 15 seconds break between tweets
import tweepy  # for twitter API
from django.utils.encoding import smart_str

# Twitter Access Tokens
from config import *

# Connecting to twitter service
AUTH = tweepy.OAuthHandler(consumer_key, consumer_secret)
AUTH.set_access_token(access_token, access_token_secret)
API = tweepy.API(AUTH)

TWEETS = []  # For collection of all tweets it acts as db for tweets
NAMES = []   # For collection of all user ids it acts as db for userids

# Follows all the followers
for follower in tweepy.Cursor(API.followers).items(100):
    follower.follow()

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
                    # retweet the tweet with searchterms
                    tweet.retweet()
                    # likes the tweet with searchterms
                    tweet.favorite()
                    # Prevents from retweeting its own tweets
                    if smart_str(tweet.author.screen_name) != volunteertwitterhandle:
                        #retweeting with comment
                        twitter = "https://twitter.com"
                        url = twitter + "/" + tweet.author.screen_name+\
                              "/" + "status" + "/" + str(tweet.id)
                        perfect = smart_str("#PyConIndia2018"+ " " +\
                                            "#pyconindia" + " " +\
                                            "#PyConIndia \n" +  url)
                        API.update_status(perfect)
                        print("Retweeted with comment of -" +tweet.author.screen_name)
                except tweepy.TweepError:
                    pass

    for i in NAMES:
        try:
        # Following the person who tweeted with #PyConIndia #PyConIndia2018
            API.create_friendship(i)
        except tweepy.TweepError:
            pass
    time.sleep(15)
