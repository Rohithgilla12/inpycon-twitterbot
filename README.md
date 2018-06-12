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

```
pip3 install -r requirements.txt --user 
```
    
### Creating Twitter API Credentials

1. Go to the [https://apps.twitter.com/](https://apps.twitter.com/)
2. Click the `Create App` button
2. Fill the necessary details for your application that you are creating
    * Name of the bot
    * Website name
    * Description
3. Once created, goto `Keys and Tokens` section and generate your access tokens.
4. Once located, move on to the next step for configuring [scripts/config.py](https://github.com/Rohithgilla12/inpycon-twitterbot/blob/master/scripts/config.py)


### Configuring Tweepy API

- For the bot to run, the Tweepy API needs to be authorised with `consumer_key`, `consumer_secret`, `access_token` and `access_token_secret`. These values are listed in [scripts/config.py](https://github.com/Rohithgilla12/inpycon-twitterbot/blob/master/scripts/config.py) and needs to be filled before the execution of `main.py` script for connecting to the Twitter API

- `searchterms` in [config.py](https://github.com/Rohithgilla12/inpycon-twitterbot/blob/master/scripts/config.py) are the      target terms, the bot checks for these terms constantly, so for example, if the user is searching for `PyConIndia2018`so the terms in the list are as follows ["#PyConIndia2018","PyConIndia","@pyconindia","#pyconindia"]
 
- Add hashtags, specific words, user handles in the `searchterms`. Anything you want retweeted.

### Running the Bot
 
- Navigate to the scripts directory and run the bot using the following command
```
  python3 main.py
```

### Hosting on Heroku

Use the following commands to host this app in heroku
```bash
heroku create
git add .
git commit -m "initial commit"
git push heroku master
heroku ps:scale worker=1
heroku logs --tail
```
## Contribution and Licence

Refer to the [Contributing.md](https://github.com/Rohithgilla12/inpycon-twitterbot/blob/master/CONTRIBUTING.md) for the same. The source code is under [MIT License](https://github.com/Rohithgilla12/inpycon-twitterbot/blob/master/CONTRIBUTING.md). 

[![HitCount](http://hits.dwyl.io/Rohithgilla12/PyCon-Twitter-Bot.svg)](http://hits.dwyl.io/Rohithgilla12/PyCon-Twitter-Bot)
