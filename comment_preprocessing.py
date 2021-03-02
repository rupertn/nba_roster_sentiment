import pandas as pd
import numpy as np
import re
import string
import nltk
from nltk.corpus import stopwords
from clean_rosters import nickname_dict


def remove_nicknames(name_dict, comm):
    words = comm.split()

    for word in words:
        if word in name_dict.keys():
            regex = r'\b{}\b'.format(word)
            comm = re.sub(regex, name_dict[word], comm)

    return comm


def remove_links(comm):
    return re.sub(r'[\(\[].*?[\)\]]', '', comm)


def remove_numbers(comm):
    return re.sub(r'\d+', '', comm)


def remove_punctuation(comm):
    return ''.join([char.lower() for char in comm if char not in string.punctuation + '‘’”“'])


def remove_whitespace(comm):
    return re.sub(r'\s+', ' ', comm).strip()


def remove_stopwords(stop_list, comm):
    return ' '.join([word for word in comm.split() if word not in stop_list])


def clean_comment(stop_list, name_dict, comm):

    comm = remove_links(comm)
    comm = remove_numbers(comm)
    comm = remove_punctuation(comm)
    comm = remove_whitespace(comm)
    comm = remove_nicknames(name_dict, comm)
    comm = remove_stopwords(comm)

    return comm


df = pd.read_csv('lakers_game_comments.csv')

df = df[df['comment_score'] > 0]

df['comment_body'] = df['comment_body'].str.split('\n')
df = df.explode('comment_body')

df = df.replace({'comment_body': ''}, np.nan)
df = df.dropna(subset=['comment_body'])

nltk.download('stopwords')
stop_words = stopwords.words('english')

df['comment_body'] = df['comment_body'].apply(lambda x: clean_comment(stop_words, nickname_dict, x))

# TODO: remove punctuation, links, images from comments etc.
# TODO: Standardize words.
# TODO: Find dictionary of slang words.
# TODO: Convert player abbreviations to full name.
# TODO: Add parent comment id to each comment.
