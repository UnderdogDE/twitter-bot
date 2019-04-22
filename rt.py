import tweepy
from time import sleep
from keys import *

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

for tweet in tweepy.Cursor(api.search, q='python OR twitter -java').items(15):
    try:
        print('\nRT Bot found a tweet by @' + tweet.user.screen_name + '. ' + 'Attempting to RT.')
        api.retweet(tweet.id)
        print('RTed tweet from'+ tweet.user.screen_name + ' successfully.')

        sleep(30)

    except tweepy.TweepError as error:
        print('\nError. RT not successful. Reason: ')
        print(error.reason)

    except StopIteration:
        break