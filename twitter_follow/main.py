#!/usr/bin/env python
# encoding: utf-8

from __future__ import unicode_literals

import codecs
import logging
import os
import random
import sys
import time

import tweepy

_API = None


def main():
    logging.basicConfig(
        level=logging.INFO,
        datefmt='%Y-%m-%d %H:%M:%S')

    _CONSUMER_KEY = os.environ['CONSUMER_KEY']
    _CONSUMER_SECRET = os.environ['CONSUMER_SECRET']
    _ACCESS_TOKEN = os.environ['ACCESS_TOKEN']
    _ACCESS_TOKEN_SECRET = os.environ['ACCESS_TOKEN_SECRET']

    auth = tweepy.auth.OAuthHandler(_CONSUMER_KEY, _CONSUMER_SECRET)
    auth.set_access_token(_ACCESS_TOKEN, _ACCESS_TOKEN_SECRET)

    if len(sys.argv) < 2:
        print("Usage: {} @user1 @user2".format(sys.argv[0]))
        sys.exit(2)

    global _API
    _API = tweepy.API(auth)
    follow_automatically(sys.argv[1:])


def follow_automatically(screen_names):
    global _API

    for screen_name in screen_names:
        print("Following {}".format(screen_name))
        print(_API.create_friendship(screen_name=screen_name).screen_name)
        delay = random.randrange(0, 86 * 2)  # average 86 seconds=1000 per day
        print("Waiting {} seconds".format(delay))
        time.sleep(delay)


if __name__ == '__main__':
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout)
    main()
