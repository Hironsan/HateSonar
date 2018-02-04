"""
Twitter crawler.
"""
import os

import tweepy


def load_keys():
    """Loads Twitter keys.

    Returns:
        tuple: consumer_key, consumer_secret, access_token, access_token_secret
    """
    consumer_key = os.environ.get('CONSUMER_KEY')
    consumer_secret = os.environ.get('CONSUMER_SECRET')
    access_token = os.environ.get('ACCESS_TOKEN')
    access_token_secret = os.environ.get('ACCESS_TOKEN_SECRET')

    return consumer_key, consumer_secret, access_token, access_token_secret


class TwitterAPI(object):

    def __init__(self, consumer_key, consumer_secret, access_token, access_token_secret):
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        self._api = tweepy.API(auth)

    def search(self, q):
        """Search tweets by keyword.

        Args:
            q: keyword

        Returns:
            list: tweet list
        """
        results = self._api.search(q=q)

        return results

    def search_by_user(self, screen_name, count=100):
        """Search tweets by user.

        Args:
            screen_name: screen name
            count: the number of tweets

        Returns:
            list: tweet list
        """
        results = self._api.user_timeline(screen_name=screen_name, count=count)

        return results
