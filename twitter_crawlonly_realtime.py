#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream


#Variables that contains the user credentials to access Twitter API


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        f.write(data)
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

    #print("abcd")
    f.close()

