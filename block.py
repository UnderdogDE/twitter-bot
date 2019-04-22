import tweepy
from time import sleep
from keys import *

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

for tweet in tweepy.Cursor(api.search, q='matlab').items(20):
    try:
        print('\nBlock Bot found a tweet by @' + tweet.user.screen_name + '. ' + 'Attempting to block user.')
        api.create_block(tweet.user.screen_name)
        print('Blocked successfully.')

        sleep(15)

    except tweepy.TweepError as error:
        print('\nError. block not successful. Reason: ')
        print(error.reason)

    except StopIteration:
        break