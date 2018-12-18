import twitter
import numpy as np
import pandas as pd
import time


api=twitter.Api()

def Random_tweet(string,tweet_array): # Writing random tweets into a file from each politician id
    file.write(string + "'s" + " tweet \n\n")
    file.write(str(tweet_array[np.random.randint(20)]))
    file.write("\n\n\n")

def Crawl_party(string,no_tweets): # Crawling the latest X tweets from the politician id

    user_info=api.GetUser(screen_name=string)
    user_info=user_info.AsDict()
    print(user_info)

    print("Writing last " + str(no_tweets) + " tweets...")
    print()

    f=open('/Users/anubhavjain/Desktop/Politicians_Parties/'+ string +'.txt','w+')

    count=0
    tweet_array=np.array(api.GetUserTimeline(screen_name=string))
    f.writelines(str(tweet_array))
    maxid=str(tweet_array[len(tweet_array)-1].id - 1)
    count+=len(tweet_array)

    Random_tweet(string,tweet_array)

    while(count < no_tweets):
        try:
            tweet_array = np.array(api.GetUserTimeline(screen_name=string,max_id=maxid))
            time.sleep(0.0000001)
            f.writelines(str(tweet_array))
            count += len(tweet_array)
            maxid = str(tweet_array[len(tweet_array) - 1].id - 1)

        except Exception as e:
            print(e)
            pass

    f.close()


file=open('/Users/anubhavjain/Desktop/Politicians_Parties/random_tweet_part.txt',"w+")
f1=open('/Users/anubhavjain/Desktop/Politicians_Parties/web_scrape.txt',"r")

for line in f1:
    Crawl_party(line,3200)

f1.close()
file.close()