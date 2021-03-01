import pandas as pd
import numpy as np
import re
import string
from clean_rosters import nickname_dict

df = pd.read_csv('lakers_game_comments.csv')

df = df[df['comment_score'] > 0]

df['comment_body'] = df['comment_body'].str.split('\n')
df = df.explode('comment_body')

df = df.replace({'comment_body': ''}, np.nan)
df = df.dropna(subset=['comment_body'])


def remove_nicknames(name_dict, comm):
    words = comm.split()

    for word in words:
        for key, item in name_dict.items():
            if word == key:
                regex = r'\b{}\b'.format(word)
                comm = re.sub(regex, item, comm)

    return comm


def remove_noise(name_dict, comm):

    comm = re.sub(r'[\(\[].*?[\)\]]', '', comm)  # removes all text and brackets inside () or [].
    # comm = re.sub(r'\d+', '', comm)  # removes numbers
    comm = ''.join([char.lower() for char in comm if char not in string.punctuation + '‘'])
    comm = re.sub(r'\s+', ' ', comm).strip()  # removes extra whitespaces

    comm = remove_nicknames(name_dict, comm)

    return comm


df['comment_body'] = df['comment_body'].apply(lambda x: remove_noise(nickname_dict, x))

# TODO: remove punctuation, links, images from comments etc.
# TODO: Standardize words.
# TODO: Find dictionary of slang words.
# TODO: Convert player abbreviations to full name.
# TODO: Add parent comment id to each comment.
