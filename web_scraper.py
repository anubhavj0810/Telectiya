import requests
from bs4 import BeautifulSoup

r=requests.get("https://www.socialbakers.com/statistics/twitter/profiles/india/society/politics/page-1-5/")
c=r.content

soup=BeautifulSoup(c,"html.parser")
#print(soup.prettify())

names=soup.find_all("div",{"class":"item"})
#print(names)

file=open('/Users/anubhavjain/Desktop/Politicians_Parties/web_scrape.txt',"w+")
count=0
m=[]

for name in names:
    a=name.find_all({"h2":"span"})
    if(len(a)>0):
        m=a[0].text.split('(')[1][:-1]
        #print(m)
        file.write(m+"\n")
        count+=1

file.close()

print("\nNo. of politicians are ...")
print(count)
