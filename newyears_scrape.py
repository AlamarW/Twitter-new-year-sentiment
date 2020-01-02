import tweepy
import csv


consumer_key = "HIDDEN"
consumer_secret = "HIDDEN"
access_token = "HIDDEN"
access_secret = "HIDDEN"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth, wait_on_rate_limit=True)

public_tweets = api.search("#IWokeUpOnJanuary1stAnd")

with open("twitter_newyear_pull.csv", 'a') as csvfile:
    csv_writer = csv.writer(csvfile)
    for tweet in tweepy.Cursor(api.search, q="#IWokeUpOnJanuary1stAnd",
                                count=1000,
                                lang="en").items():
        csv_writer.writerow([tweet.text.encode('utf-8')])
