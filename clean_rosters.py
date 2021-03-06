import pandas as pd


def get_initials(name):
    words = name.replace('-', ' ').split()
    return ''.join([word[0] for word in words])


def player_returned(p_list, season_player):
    if season_player[0] == 2021:
        return None
    elif [season_player[0] + 1, season_player[1]] in p_list:
        return 1
    else:
        return 0


df = pd.read_csv('data/rosters.csv')

# Fixing incorrect name formats
df.loc[df['name'] == 'Devontae Cacok\xa0\xa0(TW)', 'name'] = 'Devontae Cacok'
df.loc[df['name'] == 'Kostas Antetokounmpo\xa0\xa0(TW)', 'name'] = 'Kostas Antetokounmpo'
df.loc[df['name'] == 'Dennis Schröder', 'name'] = 'Dennis Schroder'

df[['first_name', 'last_name']] = df['name'].str.split(expand=True)

df['initials'] = df['name'].apply(lambda x: get_initials(x))

df['season_player'] = [list(a) for a in (zip(df.season, df.name))]
player_list = df['season_player'].to_list()

df['returned'] = df.apply(lambda row: player_returned(player_list, row['season_player']), axis=1)

df['season'] = df['season'].astype(str)

roster_train = df[df['season'] != '2021']
roster_test = df[df['season'] == '2021']
roster_full = df.copy()

roster_full.to_csv('data/roster_clean.csv', index=False)
roster_train.to_csv('data/roster_train.csv', index=False)
roster_test.to_csv('data/roster_test.csv', index=False)
