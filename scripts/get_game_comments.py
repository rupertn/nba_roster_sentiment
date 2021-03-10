import praw
import pandas as pd
from datetime import datetime


def get_search_query(opponent):
    return 'title:post game thread {}'.format(opponent)


def create_post_dict():
    submission_dict = {
        'title': [],
        'id': [],
        'score': [],
        'num_comms': [],
        'created': []
    }

    return submission_dict


def create_comment_dict():
    comm_dict = {
        'post_id': [],
        'comment_id': [],
        'comment_body': [],
        'comment_score': []
    }

    return comm_dict


def get_submission_details(post):
    post_dict['title'].append(post.title)
    post_dict['id'].append(post.id)
    post_dict['score'].append(post.score)
    post_dict['num_comms'].append(post.num_comments)
    post_dict['created'].append(post.created_utc)


def get_comment_details(post, comm):
    comments_dict['post_id'].append(post.id)
    comments_dict['comment_id'].append(comm.id)
    comments_dict['comment_body'].append(comm.body)
    comments_dict['comment_score'].append(comm.score)


def export_data(franchise, posts, comments):
    posts_df = pd.DataFrame(posts)
    comments_df = pd.DataFrame(comments)

    posts_df.to_csv('{}_game_posts.csv'.format(franchise), index=False)
    comments_df.to_csv('{}_game_comments.csv'.format(franchise), index=False)


team_subs = ['lakers']

df = pd.read_csv('nba_teams.csv')
df = df[~df['team_name'].isin(team_subs)]
nba_teams = df['team_name'].to_list()

reddit = praw.Reddit(
    client_id="",
    client_secret="",
    user_agent="",
    username="",
    password=""
)

for sub in team_subs:
    team_sub = reddit.subreddit(sub)

    post_dict = create_post_dict()
    comments_dict = create_comment_dict()

    for team in nba_teams:
        start = datetime.now()
        query = get_search_query(team)

        for submission in team_sub.search(query, sort='new', limit=None):
            get_submission_details(submission)

            submission.comments.replace_more(limit=0)
            for comment in submission.comments.list():
                get_comment_details(submission, comment)

        print('Completed comment collection for {}-{} games in {}'.format(sub, team, datetime.now()-start))

    export_data(sub, post_dict, comments_dict)
    print('Finished exporting reddit comments!')
