import twitter
import json
import numpy as np
import pandas as pd
import time


api=twitter.Api(access_token_key= ACCESS_KEY,
access_token_secret = ACCESS_SECRET,
consumer_key = CONSUMER_KEY,
consumer_secret = CONSUMER_SECRET
)

from TwitterSearch import *

def Random_tweet(string,tweet): # Writing random tweet from latest 25 into a file from each politician id
    file.write(string + "'s" + " tweet \n\n")
    file.write(str(tweet))
    file.write("\n\n\n")

def Crawl_party(string): # Crawling the latest X tweets from the politician id

    user_info=api.GetUser(screen_name=string)
    user_info=user_info.AsDict()
    print(user_info["screen_name"])

    print("Extracting latest tweets...")

    f=open('/Users/anubhavjain/Desktop/Politicians_Parties/'+ string +'.txt','w+')

    try:
        tuo = TwitterUserOrder(string)  # create a TwitterUserOrder

        """tso = TwitterSearchOrder()

        tso.set_keywords(['BJP', 'INC', 'AAP'])  # let's define all words we would like to have a look for
        tso.set_language(lang='en')
        tso.set_include_entities(False)"""

        # it's about time to create TwitterSearch object again
        ts = TwitterSearch(consumer_key=CONSUMER_KEY, consumer_secret=CONSUMER_SECRET, access_token=ACCESS_KEY,
                           access_token_secret=ACCESS_SECRET)

        """for tweet in ts.search_tweets_iterable(tso):
            print('@%s tweeted: %s' % (tweet['user']['screen_name'], tweet['text']))"""

        # start asking Twitter about the timeline

        ran = np.random.randint(25)
        count = 0
        for tweet in ts.search_tweets_iterable(tuo):
            count += 1
            f.write(str(tweet) + "\n")

            if(count==ran):
                Random_tweet(string,tweet)
            #print( '@%s tweeted: %s' % ( tweet['user']['screen_name'], tweet['text'] ) )

        print("Extracted latest",str(count),"tweets")

    except TwitterSearchException as e:  # catch all those ugly errors
        print(e)

    f.close()


file=open('/Users/anubhavjain/Desktop/Politicians_Parties/random_tweet_part.txt',"w+")
f1=open('/Users/anubhavjain/Desktop/Politicians_Parties/web_scrape.txt',"r")


t_before=time.time()
for line in f1:
    Crawl_party(line)
t_after = time.time()

print("Time taken to extract is ...")
print(t_after - t_before)
print()

f1.close()
file.close()