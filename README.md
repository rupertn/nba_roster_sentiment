# Can NBA Player Sentiment Be a Predictor for Annual Roster Turnover?
Over the course of a season, NBA fanbases will formulate opinions of their team's players based on their in-game performance. However, through team roster decisions, it can often feel as though these opinions aren't shared with the management personnal of the team. This raises the question, how closely aligned, if at all, are fanbases opinions of their players with management's annual roster movements? Do players who performed poorly in the eyes of the fanbase tend to fail to secure a roster spot for the following season? Similarly, do players who were viewed favourably by the fanbase typically return to the team? Lastly, using the fanbases opinions, can we predict which players from the 2020-2021 roster will be back next season?

To try to answer these questions I collected more than 110,000 Reddit comments from the Los Angeles Lakers subreddit, /r/lakers, and performed a sentiment analysis to gauge the fanbase's opinion of their players. Utilizing the Python Reddit API Wrapper, PRAW, comments were gathered from approximately 420 post-game threads spanning 6 seasons. As suggested by the name, a post-game thread is a comment thread posted after the game that allows for the expression of thoughts towards the teams or individual players performance. 

## Tools used:
* Languages: Python
* Packages: pandas, requests, re, nltk, beautifulsoup4, praw

## Data Collection

### Los Angeles Lakers Rosters (Current and Historical)
Roster information by season was collected from [Basketball Reference](https://www.basketball-reference.com) using a simple Python web scraper. The script, [get_team_rosters.py](https://github.com/rupertn/nba_roster_turnover/blob/main/get_team_rosters.py), downloads a single csv file and can be easily modified by adjusting the input parameters to collect roster information from any team or season available on the website. 
### Reddit Post-Game Thread Comments
Post-game comments were collected with the help of the useful Python library, PRAW, a wrapper for the Reddit API. Unfortunately the Reddit API has a response limit of 100 posts per request, and with no method of searching posts by timestamp, keeping under this limit required using a Reddit search query with keywords ('post', 'game' 'thread', {game opponent} etc.) to identify post-game threads. Consequently, post-game threads with titles that did not match the keyword search were not retrieved. However, as shown below, this method managed to acquire at least 85% of all post-game threads for each of the past 5 full NBA seasons.

| NBA Season  | Posts Collected (% Total Games)| Total Comments |
| ------------- | ------------- | ------------- |
| 2015 - 2016  | 70 (85%) | 4,670 |
| 2016 - 2017  | 72 (88%) | 10,156 |
| 2017 - 2018  | 72 (88%) | 19,120 |
| 2018 - 2019  | 81 (99%) | 29,198 |
| 2019 - 2020  | 89 (97%) | 35,951 |
| 2020 - 2021  | 33 (season in progress) | 10,362 |

## Data Cleaning
### Roster Information
### Reddit Post-Game Thread Comments


## Sentiment Analysis
## Discussion
