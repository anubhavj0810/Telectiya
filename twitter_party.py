import twitter
import numpy as np
import pandas as pd


api=twitter.Api()
file=open('/Users/anubhavjain/Desktop/random_tweet_part.txt',"w+")


print(api.GetUser(screen_name='@BJP4India'))
print("Writing last 200 tweets...")
print()

f=open('/Users/anubhavjain/Desktop/Twitter_fold/BJP.txt','w+')
count=0
a=np.array(api.GetUserTimeline(screen_name='@BJP4India'))
f.writelines(str(a))
maxid=str(a[len(a)-1].id - 1)
count+=len(a)

file.write("BJP's tweet \n\n")
file.write(str(a[np.random.randint(20)]))
file.write("\n\n\n")

while(count<200):
    a=np.array(api.GetUserTimeline(screen_name='@BJP4India',max_id=maxid))
    f.writelines(str(a))
    count+=len(a)
    maxid=str(a[len(a)-1].id -1)

f.close()

print(api.GetUser(screen_name='@INCIndia'))
print("Writing last 200 tweets...")
print()

f=open('/Users/anubhavjain/Desktop/Twitter_fold/Congress.txt','w+')
count=0
a=np.array(api.GetUserTimeline(screen_name='@INCIndia'))
f.writelines(str(a))
maxid=str(a[len(a)-1].id - 1)
count+=len(a)

file.write("INC's tweet \n\n")
file.write(str(a[np.random.randint(20)]))
file.write("\n\n\n")

while(count<200):
    a=np.array(api.GetUserTimeline(screen_name='@INCIndia',max_id=maxid))
    f.writelines(str(a))
    count+=len(a)
    maxid=str(a[len(a)-1].id -1)

f.close()

print(api.GetUser(screen_name='@AamAadmiParty'))
print("Writing last 200 tweets...")
print()

f=open('/Users/anubhavjain/Desktop/Twitter_fold/AAP.txt','w+')
count=0
a=np.array(api.GetUserTimeline(screen_name='@AamAadmiParty'))
f.writelines(str(a))
maxid=str(a[len(a)-1].id - 1)
count+=len(a)

file.write("AAP's tweet \n\n")
file.write(str(a[np.random.randint(20)]))
file.write("\n\n\n")

while(count<200):
    a=np.array(api.GetUserTimeline(screen_name='@AamAadmiParty',max_id=maxid))
    f.writelines(str(a))
    count+=len(a)
    maxid=str(a[len(a)-1].id -1)

f.close()

file.close()



