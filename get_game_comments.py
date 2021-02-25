import praw
import pandas as pd

reddit = praw.Reddit(
    client_id="my client id",
    client_secret="my client secret",
    user_agent="my user agent",
    username="rupertn28",
    password="my password"
)

# Input parameters
months = ['jan', 'january', 'feb', 'february', 'mar', 'march', 'apr', 'april', 'may', 'jun', 'june', 'oct', 'october',
          'nov', 'november', 'dec', 'december']
years = ['2017', '2018', '2019', '2020', '2021']
nba_subs = ['bostonceltics']


def get_search_query(m, yr):
    return 'title:game thread {} {}'.format(m, yr)


def create_post_dict():
    submission_dict = {
        'title': [],
        'score': [],
        'num_comms': [],
        'created': [],
    }

    return submission_dict


def create_comment_dict():
    comm_dict = {
        'post_title': [],
        'comment_id': [],
        'comment_body': [],
        'comment_score': []
    }

    return comm_dict


def get_submission_details(post):
    post_dict['title'].append(post.title)
    post_dict['score'].append(post.score)
    post_dict['num_comms'].append(post.num_comments)
    post_dict['created'].append(post.created_utc)


def get_comment_details(post, comm):
    comments_dict['post_title'].append(post.title)
    comments_dict['comment_id'].append(comm.id)
    comments_dict['comment_body'].append(comm.body)
    comments_dict['comment_score'].append(comm.score)


def export_data(team, posts, comments):
    posts_df = pd.DataFrame(posts)
    comments_df = pd.DataFrame(comments)

    posts_df.to_csv('{}_game_posts.csv'.format(team), index=False)
    comments_df.to_csv('{}_game_comments.csv'.format(team), index=False)


for sub in nba_subs:
    team_sub = reddit.subreddit(sub)

    post_dict = create_post_dict()
    comments_dict = create_comment_dict()

    for year in years:
        for month in months:
            query = get_search_query(month, year)

            for submission in team_sub.search(query, sort='new', limit=None):
                get_submission_details(submission)

                submission.comments.replace_more(limit=None)
                for comment in submission.comments.list():
                    get_comment_details(submission, comment)

    export_data(sub, post_dict, comments_dict)
