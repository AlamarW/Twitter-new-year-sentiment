import csv
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt

plt.style.use('ggplot')

sentiment_vectors = []
with open('twitter_newyears_scrape.tsv', 'r') as csvfile:
    analyzer = SentimentIntensityAnalyzer()
    for tweet in csvfile:
        vs = analyzer.polarity_scores(tweet)
        sentiment_vectors.append(vs)

positive = 0
negative = 0

for sentiment in sentiment_vectors:
    if sentiment['compound'] > 0:
        positive += 1
    else:
        negative += 1

print("Positive: ", positive)
print("Negative: ", negative)

x = ["positive", "negative"]
y = [positive, negative]
plt.title('Twitter #IWokeUpOnJanuary1stAnd Sentiment Analysis')
plt.xlabel('Sentiment')
plt.ylabel('Count')
plt.bar(x,y)
plt.show()
