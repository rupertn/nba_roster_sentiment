import pandas as pd

rosters = pd.read_csv('rosters.csv')
df = rosters.copy()

# Fixing incorrect name formats
df.loc[df['name'] == 'Devontae Cacok\xa0\xa0(TW)', 'name'] = 'Devontae Cacok'
df.loc[df['name'] == 'Kostas Antetokounmpo\xa0\xa0(TW)', 'name'] = 'Kostas Antetokounmpo'

df['season_player'] = [list(a) for a in (zip(df.season, df.name))]
player_list = df['season_player'].to_list()


def player_returned(p_list, season_player):
    if season_player[0] == 2021:
        return None
    elif [season_player[0] + 1, season_player[1]] in p_list:
        return 1
    else:
        return 0


df['returned'] = df.apply(lambda row: player_returned(player_list, row['season_player']), axis=1)

df['season'] = df['season'].astype(str)

roster_train = df[df['season'] != '2021']
roster_test = df[df['season'] == '2021']

roster_train.to_csv('roster_train.csv', index=False)
roster_test.to_csv('roster_test.csv', index=False)
