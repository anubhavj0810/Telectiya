
# In[1]:

import json
import pandas as pd
import matplotlib
import numpy as np

matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

tweets_data=[]
file=open('/Users/anubhavjain/Desktop/twitter_data_1.txt','r')

for line in file:
    try:
        tweet=json.loads(line)
        tweets_data.append(tweet)
    except(Exception):
        continue

file.close()

tweets_data=np.array(tweets_data)

print("Tweets till now are ... ")
print(len(tweets_data))


tweets_twi = pd.DataFrame()

tweets_twi['text']=list(map(lambda t:t['text'],tweets_data))
tweets_twi['lang']=list(map(lambda t:t['lang'],tweets_data))
tweets_twi['area']=list(map(lambda t:t['place']['name'] if(t['place']!= None) else None,tweets_data))
tweets_twi['country']=list(map(lambda t:t['place']['country'] if(t['place']!= None) else None,tweets_data))


tweets_by_lang = tweets_twi['lang'].value_counts()

fig, ax = plt.subplots()
ax.tick_params(axis='x', labelsize=15)
ax.tick_params(axis='y', labelsize=10)
ax.set_xlabel('Languages', fontsize=15)
ax.set_ylabel('Number of tweets' , fontsize=15)
ax.set_title('Top 5 languages in dataset', fontsize=15, fontweight='bold')
tweets_by_lang[:2].plot(ax=ax, kind='bar', color='green')
plt.show()


tweets_by_country = tweets_twi['country'].value_counts()

fig, ax = plt.subplots()
ax.tick_params(axis='x', labelsize=15)
ax.tick_params(axis='y', labelsize=10)
ax.set_xlabel('Countries', fontsize=15)
ax.set_ylabel('Number of tweets' , fontsize=15)
ax.set_title('Top 5 countries in dataset', fontsize=15, fontweight='bold')
tweets_by_country[:5].plot(ax=ax, kind='bar', color='blue')
plt.show()

