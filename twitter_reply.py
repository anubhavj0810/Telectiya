import tweepy
from tweepy import OAuthHandler
from tweepy import Cursor
import sys
from TwitterSearch import *

auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

api = tweepy.API(auth,wait_on_rate_limit=True)
name = '@BJP4India'
replies=[]
non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)

ts = TwitterSearch(consumer_key = CONSUMER_KEY,consumer_secret = CONSUMER_SECRET,access_token = ACCESS_KEY,access_token_secret = ACCESS_SECRET)
tuo = TwitterUserOrder(name) # create a TwitterUserOrder
count = 0
for full_tweets in ts.search_tweets_iterable(tuo):
    count +=1
    since = full_tweets['id']
    #print(since)
    try:
        name1 = '@' + full_tweets['retweeted_status']['user']['screen_name']
    except Exception:
        name1 = '@BJP4India'
    print(name1)
    for tweet in Cursor(api.search ,q='to:' + name1 ,since_id = since , result_type ='recent' , timeout = 999999).items(1000):
        #print(tweet.text)
        if hasattr(tweet, 'in_reply_to_status_id_str'):
            if(tweet.in_reply_to_status_id_str == full_tweets['id_str']):
                replies.append(tweet.text)
                #print(tweet.text)

    print("Tweet :",full_tweets['text'].translate(non_bmp_map))
    print("No. of replies is ..",len(replies))
    for elements in replies:
        print("Replies :",elements)
    replies.clear()