# PyCon-Twitter-Bot

[![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)](https://forthebadge.com) [![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)

## Pre-requisites 
1. Twitter Account
    
2. Modules required
    * tweepy
    * time
    * django.utils.encoding
    
### Installation

```bash
pip install requirements.txt  
```

### Creating twitter api credentials

1. Go to the following [link](https://apps.twitter.com/ "Twitter App").
2. Click the create app button
2. Fill the necessary details like :
    * Name of the bot.
    * Website name.
    * Description.
3. Goto Keys and tokens and generate your access tokens.


### Using the tweepy api

Authorise the app with tweepy api with consumer keys and access tokens.
Now replace the credentials in the code with your credentials and search hashtags with
the one which you wanted and enjoy the app up and running.



### Hosting in heroku

Use the following commands to host this app in heroku
```bash
heroku create
git add .
git commit -m "initial commit"
git push heroku master
heroku ps:scale worker=1
heroku logs --tail
```

[![HitCount](http://hits.dwyl.io/Rohithgilla12/PyCon-Twitter-Bot.svg)](http://hits.dwyl.io/Rohithgilla12/PyCon-Twitter-Bot)
