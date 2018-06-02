
import tweepy
import time

# Twitter Access Tokens

consumer_key = "fTalKjuU4FfrkmoWMmLf9zHAD"
consumer_secret = "DOZ6GlHAoXw58m4OKqFIQge5LVBpFegKlZG4qZ4Iq4jyvX1dte"
access_token = "999286008934879233-EnGV1EYEZsXpFL9wLKwRD2nAiD4fbLs"
access_token_secret = "G1jXMFYrwAdR349DFWoeVMNC0cAkvWJDvtjUOqBEYzGMk"

# Connecting to twitter service

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

tweets=[]
names=[]
namesperson=[]
while True:
    for tweet in tweepy.Cursor(api.search,q="#PyConIndia2018").items(10):
        if tweet in tweets:
            pass
        else:
            tweets.append(tweet.text)
            if(tweet.author.id not in names):
                names.append(tweet.author.id)
                namesperson.append(tweet.user.name)

            try:
                tweet.retweet()
                print("Done")
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
                tweet.retweet()
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
                tweet.retweet()
                print("Retweeted")
            except:
                pass
    for i in names:
        try:
            api.create_friendship(i)
        except:
            pass
    time.sleep(15)
