import pandas as pd
import numpy as np
import re
import string
from player_dictionaries import nicknames
from player_dictionaries import first_to_full
from player_dictionaries import last_to_full
from player_dictionaries import skip_last
from player_dictionaries import skip_first
from slang import slang_dict
from contractions import contr_dict
from nltk.corpus import stopwords


def make_lowercase(comm):
    return comm.lower()


def remove_links(comm):
    return re.sub(r'[\(\[].*?[\)\]]', '', comm)


def remove_numbers(comm):
    return re.sub(r'\d+', '', comm)


def expand_contractions(cont_dict, comm):
    for word in comm.split():
        if word in cont_dict.keys():
            name_regex = r'\b{}\b'.format(word)
            comm = re.sub(name_regex, cont_dict[word], comm)

    return comm


def remove_punctuation(comm):
    return ''.join([char for char in comm if char not in string.punctuation + '‘’”“'])


def remove_whitespace(comm):
    return re.sub(r'\s+', ' ', comm).strip()


def remove_stopwords(stop_words, comm):
    return ' '.join([word for word in comm.split() if word not in stop_words])


def remove_abbreviations(abb_dict, name_dict, comm):
    for word in comm.split():
        if word in name_dict.keys():
            name_regex = r'\b{}\b'.format(word)
            comm = re.sub(name_regex, name_dict[word], comm)

        if word in abb_dict.keys():
            abb_regex = r'\b{}\b'.format(word)
            comm = re.sub(abb_regex, abb_dict[word], comm)

    return comm


def clean_comment(stop_words, cont_dict, abb_dict, name_dict, comm):
    """Calls various functions required to clean the comment."""

    comm = make_lowercase(comm)
    comm = remove_links(comm)
    comm = remove_numbers(comm)
    comm = expand_contractions(cont_dict, comm)
    comm = remove_punctuation(comm)
    comm = remove_whitespace(comm)
    comm = remove_abbreviations(abb_dict, name_dict, comm)
    comm = remove_stopwords(stop_words, comm)

    return comm


def match_names(name_list, comm):
    return [name for name in name_list if name in comm]


def match_players(full, first, last):
    players = []

    for name in full:
        players.append(name)

    for name in first:
        if name not in skip_first and first_to_full[name] not in full:
            players.append(first_to_full[name])

    for name in last:
        if name not in skip_last and last_to_full[name] not in full:
            players.append(last_to_full[name])

    return players


c = pd.read_csv('data/lakers_game_comments.csv')
r = pd.read_csv('data/roster_clean.csv')

c = c[c['comment_score'] > 0]

c['comment_body'] = c['comment_body'].str.split('\n')
c = c.explode('comment_body')

stopwords = stopwords.words('english')

c['comment_body'] = c['comment_body'].apply(lambda x: clean_comment(stopwords, contr_dict, slang_dict,
                                                                    nicknames, x))

c = c.replace({'comment_body': ''}, np.nan)
c = c.dropna(subset=['comment_body'])

full_names = list(r['name'].str.lower().unique())
first_names = list(r['first_name'].str.lower().unique())
last_names = list(r['last_name'].str.lower().unique())

c['p_full'] = c['comment_body'].apply(lambda x: match_names(full_names, x))
c['p_first'] = c['comment_body'].apply(lambda x: match_names(first_names, x))
c['p_last'] = c['comment_body'].apply(lambda x: match_names(last_names, x))
c['p_match'] = c.apply(lambda row: match_players(row['p_full'], row['p_first'], row['p_last']), axis=1)


c_out = c[['post_id', 'comment_id', 'comment_body', 'comment_score', 'p_match']]
c_out = c_out.dropna(subset=['p_match'])

c_out.to_csv('data/lakers_game_comments_clean.csv', index=False)
