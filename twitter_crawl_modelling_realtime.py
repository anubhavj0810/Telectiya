# Code for extracting the data on basis of given keywords and modelling it

# Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

import json
import pandas as pd
import matplotlib
import numpy as np
import nltk

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
        tweet_count=tweet_count + 1

        if(count_temp==0):
            print("The following are the features of the data/tweets")
            for key in tweet.keys():
                print(key)

            print(end="\n")


        tweets_twi=tweets_twi.append({'text':tweet['text']},ignore_index = True)
        #tweets_twi=pd.concat([pd.DataFrame([tweet['lang']], columns=['lang'])],ignore_index = True)
        tweets_twi = tweets_twi.append({'lang': tweet['lang']}, ignore_index=True)
        tweets_twi = tweets_twi.append({'username': tweet['user']['name']}, ignore_index=True)


        if(tweet['user']['location']!= None):
            tweets_twi = tweets_twi.append({'user_loc': tweet['user']['location'].split(',')[0].strip().upper()}, ignore_index=True)
            #tweets_twi = tweets_twi.append({'user_country': tweet['user']['location'].split(',')}, ignore_index=True)

        else:
            tweets_twi = tweets_twi.append({'user_loc': tweet['user']['location']}, ignore_index=True)
            #tweets_twi = tweets_twi.append({'user_country': tweet['user']['location']}, ignore_index=True)

        if(tweet['place'] != None):
            #tweets_twi=tweets_twi.append({'area':tweet['place']['name']},ignore_index = True)
            tweets_twi=tweets_twi.append({'country':tweet['place']['country'].upper()},ignore_index = True)

        else:
            #tweets_twi = tweets_twi.append({'area': None}, ignore_index=True)
            tweets_twi = tweets_twi.append({'country': None}, ignore_index=True)



        tweets_by_lang = tweets_twi['lang'].value_counts()

        if(len(tweets_by_lang)>=2 and count_temp % 200 == 0):
            fig, ax = plt.subplots()
            ax.tick_params(axis='x', labelsize=15)
            ax.tick_params(axis='y', labelsize=10)
            ax.set_xlabel('Languages', fontsize=15)
            ax.set_ylabel('Number of tweets', fontsize=15)
            ax.set_title('Top 3 languages', fontsize=15, fontweight='bold')
            tweets_by_lang[:3].plot(ax=ax, kind='bar', color='green')

            f = open('/Users/anubhavjain/Desktop/Contents_twitter.txt', 'w+')
            f.write("Tweet Count till now .. \n")
            f.write(str(tweet_count))
            f.write("\n\nTop 3 Languages\n")
            f.writelines(str(tweets_by_lang[:3]))
            f.close()

            print("\nTweet Count till now .. ",end="\t")
            print(tweet_count,end="\n\n")

            #plt.show()


        tweets_by_country = tweets_twi['country'].value_counts()

        if(len(tweets_by_country)>=5 and count_temp % 200 ==0):
            fig, ax = plt.subplots()
            ax.tick_params(axis='x', labelsize=15)
            ax.tick_params(axis='y', labelsize=10)
            ax.set_xlabel('Countries', fontsize=15)
            ax.set_ylabel('Number of tweets', fontsize=15)
            ax.set_title('Top 5 countries', fontsize=15, fontweight='bold')
            tweets_by_country[:5].plot(ax=ax, kind='bar', color='blue')

            f = open('/Users/anubhavjain/Desktop/Contents_twitter.txt', 'a+')
            f.write("\n\nTop 5 Countries\n")
            f.writelines(str(tweets_by_country[:5]))
            f.close()

            #plt.show()

        tweets_by_loc = tweets_twi['user_loc'].value_counts()

        if(len(tweets_by_loc)>=5 and count_temp % 200 ==0):
            fig, ax = plt.subplots()
            ax.tick_params(axis='x', labelsize=15)
            ax.tick_params(axis='y', labelsize=10)
            ax.set_xlabel('Locations', fontsize=15)
            ax.set_ylabel('Number of tweets', fontsize=15)
            ax.set_title('Top 5 locations', fontsize=15, fontweight='bold')
            tweets_by_loc[:5].plot(ax=ax, kind='bar', color='blue')

            f = open('/Users/anubhavjain/Desktop/Contents_twitter.txt', 'a+')
            f.write("\n\nTop 5 Locations\n")
            f.writelines(str(tweets_by_loc[:5]))
            f.close()

            #plt.show()

        tweets_by_username = tweets_twi['username'].value_counts()

        if(len(tweets_by_username)>=5 and count_temp % 200 ==0):
            fig, ax = plt.subplots()
            ax.tick_params(axis='x', labelsize=15)
            ax.tick_params(axis='y', labelsize=10)
            ax.set_xlabel('UserName', fontsize=15)
            ax.set_ylabel('Number of tweets', fontsize=15)
            ax.set_title('Top 5 TwitterUsers', fontsize=15, fontweight='bold')
            tweets_by_username[:5].plot(ax=ax, kind='bar', color='blue')

            f = open('/Users/anubhavjain/Desktop/Contents_twitter.txt', 'a+')
            f.write("\n\nTop 5 TwitterUsers\n")
            f.writelines(str(tweets_by_username[:5]))
            f.close()
            #plt.show()

        #tweets_by_usercountry = tweets_twi['user_country'].value_counts()
        #print(tweets_by_usercountry)

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

    ### to write any random tweet from the dataset
    if(len(tweets_data)>0):
        f = open('/Users/anubhavjain/Desktop/Random_tweet.txt', 'w+')
        f.write("\nPrinting random tweet along with its features ....\n\n")
        for i in tweets_data[np.random.randint(len(tweets_data),size=None)].items():
            f.write(str(i) + "\n\n")
        f.close()

    tweets_twi['text'] = list(map(lambda t: t['text'], tweets_data))
    tweets_twi['lang'] = list(map(lambda t: t['lang'], tweets_data))
    #tweets_twi['area'] = list(map(lambda t: t['place']['name'] if (t['place'] != None) else None, tweets_data))
    tweets_twi['country'] = list(map(lambda t: t['place']['country'].upper() if(t['place'] != None) else None, tweets_data))
    tweets_twi['country'] = tweets_twi['country'].replace('भारत','INDIA')  ### Added the hindi written country name to english one

    tweets_twi['username'] = list(map(lambda t: t['user']['name'], tweets_data))
    tweets_twi['user_loc'] = list(map(lambda t: t['user']['location'].split(',')[0].strip().upper() if(t['user']['location'] != None and t['user']['location'].upper() != 'INDIA') else None, tweets_data))
    #tweets_twi['user_country'] = list(map(lambda t: t['user']['location'].split(',') if(t['user']['location'] != None) else None, tweets_data))



    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    file = open('/Users/anubhavjain/Desktop/twitter_data_1.txt', 'a+')

    # This line filter Twitter Streams to capture data by the given keywords and on basis of the given location as india and languages as hindi and english:
    stream.filter(track=['bjp', 'indian national congress', 'modi', 'rahul gandhi', 'bhartiya janta party'],locations=[68.1766451354, 7.96553477623, 97.4025614766, 35.4940095078],languages=['en','hi','tl'],filter_level='low')

    file.close()