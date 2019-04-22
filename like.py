import tweepy
from time import sleep
from keys import *

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

for tweet in tweepy.Cursor(api.search, q='python OR twitter -java').items(15):
    try:
        print('\nLike Bot found a tweet by @' + tweet.user.screen_name + '. ' + 'Attempting to like.')
        api.create_favorite(tweet.id)
        print('Liked tweet from'+ tweet.user.screen_name + ' successfully.')

        sleep(20)

    except tweepy.TweepError as error:
        print('\nError. Like not successful. Reason: ')
        print(error.reason)

    except StopIteration:
        break