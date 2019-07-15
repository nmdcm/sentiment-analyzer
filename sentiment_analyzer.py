import tweepy
from textblob import TextBlob
import pandas as pd

#Authenticate with Twitter API
#Replace all the strings with your credentials
consumer_key= 'Consumer key'
consumer_secret= 'Consumer secret'

access_token='Access token'
access_token_secret='Access token secret'

auth = tweepy.OAuthHandler (consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
search_term = input("Enter the keyword to search:")

#Search for tweets based on keword
public_tweets = api.search(search_term)
label = []
tw = []
sent = []

for tweet in public_tweets:
    analysis = TextBlob(tweet.text)
    if(analysis.sentiment.polarity<0):
        label.append('Negative')
    else:
        label.append('Positive')
    tw.append(tweet.text)
    sent.append(analysis.sentiment.polarity)

#Write the data to a CSV file
df = pd.DataFrame({'Tweet':tw, 'Sentiment':sent, 'Label':label})
with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
    print(df)
df.to_csv("sentiment_data.csv")
