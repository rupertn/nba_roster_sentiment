# Can NBA Player Sentiment Be a Predictor for Annual Roster Turnover?
Over the course of a season, NBA fanbases will formulate opinions of their team's players based on their in-game performance. However, through team roster decisions, it can often feel as though these opinions aren't shared with the management personnal of the team. This raises the question, how closely aligned, if at all, are fanbases opinions of their players with management's annual roster movements? Do players that performed poorly in the eyes of the fanbase tend to fail to secure a roster spot for the following season? Similarly, do players that were viewed favourably by the fanbase typically return to the team? Lastly, using the fanbases opinions, can we predict which players from the 2020-2021 roster will be back next season?

To try to answer these questions I collected more than 120,000 Reddit comments from the Los Angeles Lakers subreddit, /r/lakers, and performed a sentiment analysis to gauge the fanbase's opinion of their players. Utilizing the Python Reddit API Wrapper, PRAW, comments were gathered from approximately 450 post-game comment threads spanning 6 seasons. As suggested by the name, a post-game thread is a comment thread posted after the game that allows for the expression of thoughts towards the teams or individual players performance. 

### Tools used:
* Languages: Python
* Packages: pandas, requests, re, ntlk, beautifulsoup4, praw

### Data Collection

| NBA Season  | Posts Collected (% Total)| Total Comments |
| ------------- | ------------- | ------------- |
| 2015 - 2016  | 70 (85%) |
| 2016 - 2017  | 72 (88%) |
| 2017 - 2018  | 72 (88%) |
| 2018 - 2019  | 81 (99%) |
| 2019 - 2020  | 89 (97%) |
| 2020 - 2021  | 33 (season in progress) |


## Cavaets
