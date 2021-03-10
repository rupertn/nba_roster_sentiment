import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()

c = pd.read_csv('data/lakers_game_comments_clean.csv', converters={'p_match': eval})
p = pd.read_csv('data/game_posts_clean.csv')
r = pd.read_csv('data/roster_train.csv')

df = pd.merge(p, c, left_on='id', right_on='post_id')
df = df[df['p_match'].str.len() == 1]
df = df.explode('p_match')

df['polarity'] = df['comment_body'].apply(lambda x: analyzer.polarity_scores(x))
df['comm_sentiment'] = df['polarity'].apply(lambda x: x['compound'])

sent = df.groupby(['season', 'p_match'])['comm_sentiment'].agg(['mean', 'count']).reset_index()
sent = pd.merge(r, sent, how='left', left_on=['season', 'name'], right_on=['season', 'p_match'])

sent = sent.rename(columns={'mean': 'comm_sentiment', 'count': 'num_comments'})

sent_out = sent[['season', 'name', 'num_comments', 'comm_sentiment', 'returned']]
sent_out.to_csv('sentiment_results_full.csv', index=False)
