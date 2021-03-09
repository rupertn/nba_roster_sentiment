import pandas as pd
import requests
from bs4 import BeautifulSoup as bs
import time

# Input parameters
nba_seasons = ['2018', '2019', '2020', '2021']
nba_teams = ['LAL']  # 3 char team codes can be found by looking at the url of the team on Basketball Reference.


def get_urls(teams, seasons):
    """Collects the roster urls for specified teams and seasons."""

    urls = []
    for team in teams:
        for season in seasons:
            url = 'https://www.basketball-reference.com/teams/{}/{}.html'.format(team, season)
            urls.append(url)

    return urls


def get_roster_info(urls):
    """Collects roster information for specified teams and seasons """

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
    """Exports unaltered roster data to a csv file."""

    df = pd.DataFrame(rosters)
    df.columns = ['season', 'name', 'pos', 'height', 'weight', 'dob', 'country', 'exp', 'college']

    df.to_csv('rosters.csv', index=False)


def scrape_rosters():
    """Calls various functions to perform roster scraping."""

    print('Collecting roster information...')
    roster_urls = get_urls(nba_teams, nba_seasons)
    roster_data = get_roster_info(roster_urls)

    export_data(roster_data)
    print('Finished exporting roster information for {} team(s) over {} season(s).'.format(len(nba_teams),
                                                                                           len(nba_seasons)))


if __name__ == '__main__':
    scrape_rosters()
