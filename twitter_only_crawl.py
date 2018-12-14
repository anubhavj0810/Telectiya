#Code for extracting the data on basis of given keywords

#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

import json
import pandas as pd
import matplotlib
import numpy as np

matplotlib.use('TkAgg')
import matplotlib.pyplot as plt


#Variables that contains the user credentials to access Twitter API
access_token = "911609571885633541-4EwvGuoHKFDlXSS22WC21wWOq8qqFse"
access_token_secret = "aHsqcWUCce7rcrwh9e6vKQOwUJf2x30FXzQYbM81uMCmI"
consumer_key = "DZBKOKfoWsshSYUe1NI3ba91I"
consumer_secret = "WL3mlr7GudRbIkXRSB762MDrplwYPnAvdwXB5pwAgiYTeERNTR"

tweets_data=[]

#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        f.write(data)

        try:
            tweet=json.loads(data)
            tweets_data.append(tweet)
        except(Exception):
            continue        

        #file.close()       

        tweets_data=np.array(tweets_data)
        print(len(tweets_data))
        #print(tweets_data.shape)
        #print(type(tweets_data[0]))        

        for key in tweets_data[0].keys():
            print(key)      

        print(end="\n")     

        i=0
        while(tweets_data[i]['place'] == None):
            i=i+1
        print(i,tweets_data[i]['place'])        

        tweets_twi = pd.DataFrame()     

        tweets_twi['text']=list(map(lambda t:t['text'],tweets_data))
        tweets_twi['lang']=list(map(lambda t:t['lang'],tweets_data))
        tweets_twi['area']=list(map(lambda t:t['place']['name'] if(t['place']!= None) else None,tweets_data))
        tweets_twi['country']=list(map(lambda t:t['place']['country'] if(t['place']!= None) else None,tweets_data)) 
            

        # In[2]:    
            

        #print(tweets_twi.head().to_string())   
            

        # In[26]:   
            

        #print(tweets_twi['area'].value_counts().to_string())   
            

        # In[3]:    
            

        tweets_by_lang = tweets_twi['lang'].value_counts()      

        fig, ax = plt.subplots()
        ax.tick_params(axis='x', labelsize=15)
        ax.tick_params(axis='y', labelsize=10)
        ax.set_xlabel('Languages', fontsize=15)
        ax.set_ylabel('Number of tweets' , fontsize=15)
        ax.set_title('Top 5 languages', fontsize=15, fontweight='bold')
        tweets_by_lang[:5].plot(ax=ax, kind='bar', color='green')
        #plt.show() 
            

        # In[4]:    
            

        tweets_by_country = tweets_twi['country'].value_counts()        

        fig, ax = plt.subplots()
        ax.tick_params(axis='x', labelsize=15)
        ax.tick_params(axis='y', labelsize=10)
        ax.set_xlabel('Countries', fontsize=15)
        ax.set_ylabel('Number of tweets' , fontsize=15)
        ax.set_title('Top 5 countries', fontsize=15, fontweight='bold')
        tweets_by_country[:5].plot(ax=ax, kind='bar', color='blue')
        #plt.show()
        return True

    def on_error(self, status):
        print(status)


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    f=open('/Users/anubhavjain/Desktop/twitter_data.txt','a+')
    #This line filter Twitter Streams to capture data by the given keywords:
    stream.filter(track=['bjp', 'indian national congress', 'modi','rahul gandhi','inc','bhartiya janta party'])

    f.close()

