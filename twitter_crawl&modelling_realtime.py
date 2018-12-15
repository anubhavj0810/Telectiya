# Code for extracting the data on basis of given keywords and modelling it

# Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

import json
import pandas as pd
import matplotlib
import numpy as np

matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

# Variables that contains the user credentials to access Twitter API


# This is a basic listener that just prints received tweets to stdout.

count_temp=0

class StdOutListener(StreamListener):

    def on_data(self, data):
        global tweet_count
        global tweets_twi
        global count_temp

        file.write(data)
        tweet = json.loads(data)
        tweet_count=tweet_count+1

        """if(count_temp==-1):
            print("The following are the features of the data/tweets")
            for key in tweet.keys():
                print(key)

            print(end="\n")"""


        tweets_twi=tweets_twi.append({'text':tweet['text']},ignore_index = True)
        #tweets_twi=pd.concat([pd.DataFrame([tweet['lang']], columns=['lang'])],ignore_index = True)
        tweets_twi = tweets_twi.append({'lang': tweet['lang']}, ignore_index=True)

        """if(tweet['lang']=='tl'):
            tweets_twi = tweets_twi.append({'lang': 'hi' }, ignore_index=True)
        else:
            tweets_twi = tweets_twi.append({'lang': tweet['lang']}, ignore_index=True)"""

        if(tweet['place'] != None):
            tweets_twi=tweets_twi.append({'area':tweet['place']['name']},ignore_index = True)
            tweets_twi=tweets_twi.append({'country':tweet['place']['country']},ignore_index = True)

        else:
            tweets_twi = tweets_twi.append({'area': None}, ignore_index=True)
            tweets_twi = tweets_twi.append({'country': None}, ignore_index=True)



        tweets_by_lang = tweets_twi['lang'].value_counts()

        if(len(tweets_by_lang)>=2 and count_temp % 200 == 0):
            fig, ax = plt.subplots()
            ax.tick_params(axis='x', labelsize=15)
            ax.tick_params(axis='y', labelsize=10)
            ax.set_xlabel('Languages', fontsize=15)
            ax.set_ylabel('Number of tweets', fontsize=15)
            ax.set_title('Top 2 languages', fontsize=15, fontweight='bold')
            tweets_by_lang[:2].plot(ax=ax, kind='bar', color='green')
            print("Tweet Count till now .. ",tweet_count)
            plt.show()


        tweets_by_country = tweets_twi['country'].value_counts()

        if(len(tweets_by_country)>=5 and count_temp % 200 ==0):
            fig, ax = plt.subplots()
            ax.tick_params(axis='x', labelsize=15)
            ax.tick_params(axis='y', labelsize=10)
            ax.set_xlabel('Countries', fontsize=15)
            ax.set_ylabel('Number of tweets', fontsize=15)
            ax.set_title('Top 5 countries', fontsize=15, fontweight='bold')
            tweets_by_country[:5].plot(ax=ax, kind='bar', color='blue')
            plt.show()


        count_temp=count_temp + 1
        return True

    def on_error(self, status):
        print(status)


if __name__ == '__main__':
    # This handles Twitter authetification and the connection to Twitter Streaming API

    tweets_twi = pd.DataFrame()
    tweet_count = 0
    tweets_data=[]

    f_temp = open('/Users/anubhavjain/Desktop/twitter_data_1.txt', 'r')

    for line in f_temp:
        try:
            tweet1 = json.loads(line)
            tweets_data.append(tweet1)

        except(Exception):
            continue

    f_temp.close()

    tweets_data = np.array(tweets_data)
    tweet_count=len(tweets_data)

    ### to print any random tweet from the dataset
    print("Printing random tweet along with its features ....",end="\n\n")
    if(len(tweets_data)>0):
        for i in tweets_data[np.random.randint(len(tweets_data),size=None)].items():
            print(i)


    tweets_twi['text'] = list(map(lambda t: t['text'], tweets_data))
    tweets_twi['lang'] = list(map(lambda t: t['lang'], tweets_data))
    #tweets_twi['lang'] = tweets_twi['lang'].replace('tl','hi')   ### Added the hindi semantics written in English to the lang hindi
    tweets_twi['area'] = list(map(lambda t: t['place']['name'] if (t['place'] != None) else None, tweets_data))
    tweets_twi['country'] = list(map(lambda t: t['place']['country'] if (t['place'] != None) else None, tweets_data))


    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    file = open('/Users/anubhavjain/Desktop/twitter_data_1.txt', 'a+')

    # This line filter Twitter Streams to capture data by the given keywords and on basis of the given location as india and languages as hindi and english:
    stream.filter(track=['bjp', 'indian national congress', 'modi', 'rahul gandhi', 'bhartiya janta party'],locations=[68.1766451354, 7.96553477623, 97.4025614766, 35.4940095078],languages=['en','hi','tl'],filter_level='low')

    file.close()
