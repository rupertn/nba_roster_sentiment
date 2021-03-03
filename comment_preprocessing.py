import pandas as pd
import numpy as np
import re
import string
from clean_rosters import nickname_dict
import nltk
from nltk.corpus import stopwords


def remove_links(comm):
    return re.sub(r'[\(\[].*?[\)\]]', '', comm)


def remove_numbers(comm):
    return re.sub(r'\d+', '', comm)


def remove_punctuation(comm):
    return ''.join([char.lower() for char in comm if char not in string.punctuation + '‘’”“'])


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


def clean_comment(stop_words, abb_dict, name_dict, comm):

    comm = remove_links(comm)
    comm = remove_numbers(comm)
    comm = remove_punctuation(comm)
    comm = remove_whitespace(comm)
    comm = remove_abbreviations(abb_dict, name_dict, comm)
    comm = remove_stopwords(stop_words, comm)

    return comm


df = pd.read_csv('lakers_game_comments.csv')

df = df[df['comment_score'] > 0]

df['comment_body'] = df['comment_body'].str.split('\n')
df = df.explode('comment_body')

df = df.replace({'comment_body': ''}, np.nan)
df = df.dropna(subset=['comment_body'])

stopwords = stopwords.words('english')

abbr_dict = {
    'smh': 'shake my head',
    'tbh': 'to be honest',
    'goat': 'greatest of all time',
    'lol': 'laugh out loud',
    'lmao': 'laugh my ass off',
    'lmfao': 'laugh my fucking ass off',
    'idk': 'i dont know',
    'mvp': 'most valuable player',
    'fmvp': 'finals most valuable player',
    'goated': 'greatest of all time',
    'nah': 'no way',
    'kinda': 'kind of',
    'ngl': 'not going to lie',
    'ass': 'bad',
    'plz': 'please',
    'fts': 'free throws',
    'pts': 'points'
}

df['comment_body'] = df['comment_body'].apply(lambda x: clean_comment(stopwords, abbr_dict, nickname_dict, x))

# TODO: Standardize words
# TODO: Convert player abbreviations to full name.
# TODO: Add parent comment id to each comment.
# TODO: Drop all words with 2 chars or less
