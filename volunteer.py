#Required imports

import tweepy #for twitter API
import time   #for giving 15 seconds break between tweets
from django.utils.encoding import smart_str


# Twitter Access Tokens

from config import *

# Connecting to twitter service

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)

def get_tweets(userhandle,mode="extended"):
    return tweepy.Cursor(api.user_timeline,userhandle,tweet_mode=mode).items()

def get_tags(tweet):
    tags = []
    for hashtag in tweet.entities["hashtags"]:
        tags.append(smart_str(hashtag["text"]))
    return tags

def checkSearchTerms(searchterms,tags):
    count = 0
    tagschecklist = [y.upper() for y in tags]

    for searchitem in searchterms:
        if searchitem.upper() in tagschecklist:
            count +=1
    return (count == 2)


while api.verify_credentials() is not False:
    try:
        userTweets = get_tweets(pyconindiahandle)

        for tweet in userTweets:
            if not(tweet.retweeted):
                tags = get_tags(tweet)
                
                if checkSearchTerms(searchterms,tags):
                    tweet.retweet()
                    print("Retweeted")

        time.sleep(15)
        
    except tweepy.TweepError:
        print("Some error has been handled")
