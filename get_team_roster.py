import pandas as pd
import requests
from bs4 import BeautifulSoup as bs
from datetime import datetime
import time

"""Input parameters"""
nba_seasons = ['2018', '2019', '2020', '2021']
nba_teams = ['TOR']


def get_urls(teams, seasons):

    urls = []
    for team in teams:
        for season in seasons:
            url = 'https://www.basketball-reference.com/teams/{}/{}.html'.format(team, season)
            urls.append(url)

    return urls


def get_roster_info(urls):

    rosters = []
    for url in urls:
        page = requests.get(url)
        soup = bs(page.text, 'html.parser')

        roster_table = soup.find('table', id='roster').find('tbody')

        for row in roster_table.find_all('tr'):
            player = [url.rsplit('/', 1)[1].split('.')[0]]
            for col in row.find_all('td'):
                player.append(col.text)

            rosters.append(player)

        time.sleep(1)

    return rosters


def export_data(rosters):
    df = pd.DataFrame(rosters)
    df.columns = ['season', 'name', 'pos', 'height', 'weight', 'dob', 'country', 'exp', 'college']

    df.to_csv('raptors_rosters.csv', index=False)


def scrape_rosters():
    start = datetime.now()

    roster_urls = get_urls(nba_teams, nba_seasons)

    roster_data = get_roster_info(roster_urls)

    export_data(roster_data)


if __name__ == '__main__':
    scrape_rosters()
