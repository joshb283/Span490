import tweepy


import json
import csv




# import configparser

#config parser
# config = configparser.ConfigParser()
# config.read('config.ini')


#twitter
# api_key = config['twitter']['api_key']
# api_key_secret = config['twitter']['api_key_secret']
# access_token = config['twitter']['access_token']
# access_token_secret = config['twitter']['access_token_secret']
#bearer_token = config['twitter']['bearer_token']
#authernication
# #auth = tweepy.OAuth2BearerHandler(bearer_token)
# auth = tweepy.OAuthHandler(api_key,api_key_secret)
# auth.set_access_token(access_token,access_token_secret)
# api = tweepy.API(auth)

bearer_token = "AAAAAAAAAAAAAAAAAAAAAL0WhwEAAAAAoU8HqOk5xCJnTVN2G%2BGaCF2Qrzw%3D3Ugt3TZXhjV1xeA4OxaS41pZ7AeD48Gc1eu4sKNggeHXJQNAHV"

client = tweepy.Client(bearer_token=bearer_token)
query = '#spanglish -is:retweet'
f = open("output/output1.txt", "a")#append
tweets = client.search_recent_tweets(query=query, tweet_fields=['context_annotations', 'created_at'], max_results=10)

# g = open("output/output2.txt", "a")#append)
# for tweet in tweets.data:
#     g.write(tweet.text)

#STATIC LINK TO PUT BEFORE ID:https://twitter.com/twitter/statuses/

g = open("output/output3.csv", "w")
for tweet in tweets.data:
    s = ("https://twitter.com/twitter/statuses/"+str(tweet.id)+ ","+ tweet.text.replace(",","").replace("\n"," ")+"\n")
    g.write(s)
    # tweet.
    # json_object = json.dumps(tweet.text, indent=4)
    # g.write(json_object)
    # g.write("\n\n\n\n")
 

# for tweet in tweets.data:
#     print(tweet.text)
#     f.write(tweet)
#     if len(tweet.context_annotations) > 0:
#         print(tweet.context_annotations)
#         f.write(tweet)
#     f.write("\n\n\n")
# f.close()