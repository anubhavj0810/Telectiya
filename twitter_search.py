import json
import numpy as np
import pandas as pd
import time


import twitter
from TwitterSearch import *


def twitter_search_tweets(string,abb):
    try:
        tuo = TwitterUserOrder('@BJP4India') # create a TwitterUserOrder

        tso = TwitterSearchOrder()

        tso.set_keywords([string,abb])  # let's define all words we would like to have a look for
        tso.set_language(lang='en')
        tso.set_include_entities(False)

        # it's about time to create TwitterSearch object again
        ts = TwitterSearch(consumer_key = CONSUMER_KEY,consumer_secret = CONSUMER_SECRET,access_token = ACCESS_KEY,access_token_secret = ACCESS_SECRET)

        for tweet in ts.search_tweets_iterable(tso):
            print('@%s tweeted: %s' % (tweet['user']['screen_name'].encode('ascii', 'ignore').decode('ascii'), tweet['text'].encode('ascii', 'ignore').decode('ascii')))

        # start asking Twitter about the timeline

        """t_before = time.time()
        count=0
        for tweet in ts.search_tweets_iterable(tuo):
            count+=1
            print( '@%s tweeted: %s' % ( tweet['user']['screen_name'], tweet['text'] ) )
        print(count)
        t_after = time.time()

        print("Time taken is ...")
        print(t_after - t_before)"""
    except TwitterSearchException as e: # catch all those ugly errors
        print(e)

print("Enter the party name and its abbreviation")
string,abb = input().split()
twitter_search_tweets(string,abb)