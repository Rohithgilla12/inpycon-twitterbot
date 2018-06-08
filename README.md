# inpycon-twitterbot

[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.png?v=103)](https://github.com/ellerbrock/open-source-badges/)  ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/Django.svg) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A twitter bot made using Python and Twitter API to retweet posts using specific terms related to the conference and be beneficial to thea social media campaign by keeping all tweets about PyCon India in one place and get the event trending. 
It could be hastags, twitter handles, slang words. Anything. 

## Setup and Running the bot

### Install the Requirements 

- Fork and clone this repository, 

```
git clone <Forked repository URL>
```

- Run the following command in your terminal, be sure to have [Python3](https://www.python.org/downloads/) already setup in your system.

```bash
pip3 install -r requirements.txt --user 
```
    
### Creating Twitter API Credentials

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
