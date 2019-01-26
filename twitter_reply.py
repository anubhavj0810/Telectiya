import tweepy
from tweepy import OAuthHandler
from tweepy import Cursor
import sys
import twitter
from TwitterSearch import *


auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

api1=twitter.Api(consumer_key=CONSUMER_KEY,consumer_secret=CONSUMER_SECRET,access_token_key=ACCESS_KEY,access_token_secret=ACCESS_SECRET)

def Reply(full_tweet,c1):
    replies = dict()

    if(c1>2): ### Fixing the depth of the graph
        return replies

    if (c1 == 0):
        value = 1000
    else:
        value = 100
        full_tweet = full_tweet._json

    since = full_tweet['id']
    try:
        name = '@' + full_tweet['retweeted_status']['user']['screen_name']
        since = full_tweet['retweeted_status']['id']
    except Exception:
        name = '@' + full_tweet['user']['screen_name']

    #if (c1 == 0):
    print(name,c1)

    replies[since] = []
    c1 += 1
    for tweet in Cursor(api.search ,q='to:' + name ,since_id = since , result_type ='recent' , timeout = 999999).items(value):
        #print(tweet.text)
        if hasattr(tweet, 'in_reply_to_status_id_str'):
            if(tweet.in_reply_to_status_id_str == str(since)):
                replies[since].append(Reply(tweet,c1))
                #replies.append(tweet.text)
    c1-=1
    return replies,since




api = tweepy.API(auth,wait_on_rate_limit=True)
print("Enter the Screen Name of the political party whose tweets reply tree you want to see(eg. @BJP4India,@INCIndia,@AamAadmiParty)")
name = input()
#name = '@BJP4India'
reply_arr = []
non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)

ts = TwitterSearch(consumer_key = CONSUMER_KEY,consumer_secret = CONSUMER_SECRET,access_token = ACCESS_KEY,access_token_secret = ACCESS_SECRET)
tuo = TwitterUserOrder(name) # create a TwitterUserOrder
count = 0

for full_tweets in ts.search_tweets_iterable(tuo):
    count +=1
    c1 = 0
    reply_arr,id_tweet = Reply(full_tweets,c1)
    #print(tweet.text)

    print("Tweet :",full_tweets['text'].translate(non_bmp_map))
    print("No. of replies is ..",len(reply_arr[id_tweet]))
    for elements in reply_arr[id_tweet]:
        print("Replies :",elements)
    reply_arr.clear()