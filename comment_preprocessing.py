import pandas as pd
import numpy as np
import re
import string
from clean_rosters import nickname_dict
from comment_slang import slang_dict
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

    comm = make_lowercase(comm)
    comm = remove_links(comm)
    comm = remove_numbers(comm)
    comm = expand_contractions(cont_dict, comm)
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

df['comment_body'] = df['comment_body'].apply(lambda x: clean_comment(stopwords, contr_dict, slang_dict,
                                                                      nickname_dict, x))

# df.to_csv('lakers_game_comments_clean.csv', index=False)
# TODO: Convert player abbreviations to full name.
# TODO: Deal with emojis
# TODO: Add parent comment id to each comment.
# TODO: Drop all words with 2 chars or less

