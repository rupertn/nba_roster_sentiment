import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()

c = pd.read_csv('data/lakers_game_comments_clean.csv', converters={'p_match': eval})
p = pd.read_csv('data/game_posts_clean.csv')
r = pd.read_csv('data/roster_train.csv')

df = pd.merge(p, c, left_on='id', right_on='post_id')
df = df[(df['p_match'].str.len() == 1) & (~df['season'].isin(['2015', '2016', '2017']))]
df = df.explode('p_match')

df['polarity'] = df['comment_body'].apply(lambda x: analyzer.polarity_scores(x))
df['comm_sentiment'] = df['polarity'].apply(lambda x: x['compound'])

p_sentiment = df.groupby(['season', 'p_match'])['comm_sentiment'].mean().reset_index()
p_sentiment = pd.merge(r, p_sentiment, how='left', left_on=['season', 'name'], right_on=['season', 'p_match'])

sentiment_out = p_sentiment[['season', 'name', 'comm_sentiment', 'returned']]
