#Required imports

import tweepy #for twitter API
import time   #for giving 15 seconds break between tweets
from django.utils.encoding import smart_str


# Twitter Access Tokens

from config import *

# Connecting to twitter service

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

tweets = []  # For collection of all tweets it acts as db for tweets
names = []   # For collection of all user ids it acts as db for userids
namesperson = []  # For collection of all usernames it acts as db for user names
while True:
    for searchterm in searchterms:
        
        for tweet in tweepy.Cursor(api.search, q=searchterm).items(10):
            if tweet in tweets:
                pass
            else:
                tweets.append(tweet.text)  # AAdding the tweet to db
                if tweet.author.id not in names:  # Checking if the same person tweeted more than once
                    names.append(tweet.author.id)
                    namesperson.append(tweet.user.name)

                try:
                    # tweet.retweet()
                    # Retweet with reply feature implementaiton, using smart_str to convert unicode to string
                    if smart_str(tweet.author.screen_name)!=volunteertwitterhandle:
                        perfect = "RT @"+smart_str(tweet.author.screen_name)+" "+smart_str(tweet.text)
                        api.update_status(perfect)
                        print("Retweeted")
                except:
                    pass
    for i in names:
        try:
            api.create_friendship(i)  # Following the person who tweeted with #PyConIndia #PyConIndia2018
        except:
            pass
    time.sleep(15)
