The account activity can be monitored using one app itself i.e no need to create different apps for different political parties.

Dataset(tweets) for each political party is stored in different file.

Relevant Features which can be extracted from the latest X tweets (where we can decide the value of X) of the political parties are given below :

"favorite_count"(No. of Likes) , "retweet_count"
"lang"
"text"
"user info"
"followers_count" , "friends_count"
"statuses_count"

"quoted_status" ---- "favorite_count" , "retweet_count" , "text" , user info , "followers_count" , "friends_count" ,  "location" , "statuses_count"

"retweeted_status" ---- "favorite_count" , "retweet_count" , user info, "followers_count" , "friends_count" ,  "location" , "statuses_count"

No. of replies ---- ?(Not sure)

Also we can the friends_id and friends_name of the politician i.e. people whom he follows.

Getting the names of followers is not possible because they are in millions and thus rate limit exceeded error will come.