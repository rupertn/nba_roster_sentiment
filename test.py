import pandas as pd
import requests
from bs4 import BeautifulSoup as bs
from datetime import datetime
import time


"""Input parameters"""
nba_seasons = ['2018', '2019', '2020', '2021']
nba_teams = ['TOR']


urls = []
for team in nba_teams:
    for season in nba_seasons:
        url = 'https://www.basketball-reference.com/teams/{}/{}.html'.format(team, season)
        print(url)
        urls.append(url)


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

print(rosters)
