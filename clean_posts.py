import pandas as pd
from datetime import datetime


def get_season(season_dict, post_date):
    for season, dates in season_dict.items():
        begin = season_dict[season][0]
        end = season_dict[season][1]

        if begin <= post_date <= end:
            return season


df = pd.read_csv('data/lakers_game_posts.csv')

df = df[df['title'].str.contains('Post Game')]

df['created'] = df['created'].apply(lambda x: datetime.fromtimestamp(x))

season_dates = {
    '2016': ['2015-10-27', '2016-06-19'],
    '2017': ['2016-10-25', '2017-06-12'],
    '2018': ['2017-10-17', '2018-06-08'],
    '2019': ['2018-10-16', '2019-06-13'],
    '2020': ['2019-10-22', '2020-10-12'],
    '2021': ['2020-12-22', '2021-07-22'],
}

for key, values in season_dates.items():
    season_dates[key] = [pd.to_datetime(val) for val in values]

df['season'] = df['created'].apply(lambda x: get_season(season_dates, x))

df.to_csv('game_posts_clean.csv', index=False)
