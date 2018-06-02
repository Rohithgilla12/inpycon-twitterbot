#Required imports

import tweepy #for twitter API
import time   #for giving 15 seconds break between tweets
from django.utils.encoding import smart_str

# Twitter Access Tokens

consumer_key = "fTalKjuU4FfrkmoWMmLf9zHAD"
consumer_secret = "DOZ6GlHAoXw58m4OKqFIQge5LVBpFegKlZG4qZ4Iq4jyvX1dte"
access_token = "999286008934879233-EnGV1EYEZsXpFL9wLKwRD2nAiD4fbLs"
access_token_secret = "G1jXMFYrwAdR349DFWoeVMNC0cAkvWJDvtjUOqBEYzGMk"

# Connecting to twitter service

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

tweets=[]  # For collection of all tweets it acts as db for tweets
names=[]   # For collection of all user ids it acts as db for userids
namesperson=[] # For collection of all usernames it acts as db for user names
while True:
    for tweet in tweepy.Cursor(api.search,q="#PyConIndia2018").items(10):
        if tweet in tweets:
            pass
        else:
            tweets.append(tweet.text) #AAdding the tweet to db
            if(tweet.author.id not in names): #Checking if the same person tweeted more than once
                names.append(tweet.author.id)
                namesperson.append(tweet.user.name)

            try:
                #tweet.retweet()
                #Retweet with reply feature implementaiton, using smart_str to convert unicode to string
                if(smart_str(tweet.author.screen_name)!="BotGills"):
                    perfect = "RT @"+smart_str(tweet.author.screen_name)+" "+smart_str(tweet.text)
                    api.update_status(perfect)
                    print("Retweeted")
            except:
                pass
    for tweet in tweepy.Cursor(api.search,q="#PyConIndia").items(10):
        if tweet in tweets:
            pass
        else:
            tweets.append(tweet.text)
            if(tweet.author.id not in names):
                names.append(tweet.author.id)
                namesperson.append(tweet.user.name)
            try:
                #tweet.retweet()
                if(smart_str(tweet.author.screen_name)!="BotGills"):
                    perfect = "RT @"+smart_str(tweet.author.screen_name)+" "+smart_str(tweet.text)
                    api.update_status(perfect)
                    print("Retweeted")
            except:
                pass
    for tweet in tweepy.Cursor(api.search,q="@pyconindia").items(10):
        if tweet in tweets:
            pass
        else:
            tweets.append(tweet.text)
            if(tweet.author.id not in names):
                names.append(tweet.author.id)
                namesperson.append(tweet.user.name)
            try:
                #tweet.retweet()
                if(smart_str(tweet.author.screen_name)!="BotGills"):
                    perfect = "RT @"+smart_str(tweet.author.screen_name)+" "+smart_str(tweet.text)
                    api.update_status(perfect)
                    print("Retweeted")
            except:
                pass
    for i in names:
        try:
            api.create_friendship(i) #Following the person who tweeted with #PyConIndia #PyConIndia2018
        except:
            pass
    time.sleep(15)
