import pandas as pd

df = pd.read_csv('data/roster_clean.csv')

nicknames = dict(zip(df.initials.str.lower(), df.name.str.lower()))

nicknames['kuz'] = 'kyle kuzma'
nicknames['bron'] = 'lebron james'
nicknames['lbj'] = 'lebron james'
nicknames['zu'] = 'ivica zubac'
nicknames['zo'] = 'lonzo ball'
nicknames['wes'] = 'wesley matthews'
nicknames['kief'] = 'markieff morris'
nicknames['kieff'] = 'markieff morris'

del nicknames['am']
del nicknames['it']
del nicknames['js']

# TODO: deal with JR abbreviation

first_to_full = dict(zip(df.first_name.str.lower(), df.name.str.lower()))
last_to_full = dict(zip(df.last_name.str.lower(), df.name.str.lower()))
