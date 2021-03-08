# Can NBA Player Sentiment Be a Predictor for Annual Roster Turnover?
Over the course of a season, NBA fanbases will formulate opinions of their team's players based on their in-game performance. However, through team roster decisions, it can often feel as though these opinions aren't shared with the management personnal of the team. This raises the question, how closely aligned, if at all, are fanbases opinions of their players with managements annual roster movements? Do players that performed poorly in the eyes of the fanbase tend to fail to secure a roster spot for the following season? Similarly, do players that were viewed favourably by the fanbase typically return to the team? Lastly, using the fanbases opinions, can we predict which players from the 2020-2021 roster will be back next season?

To try to answer these questions I collected more than 120,000 comments from the Los Angeles Lakers subreddit, /r/lakers, and performed a sentiment analysis to gauge the fanbase's opinion of their players. Comments were gathered using the Python Reddit API Wrapper, PRAW, and targeted the post-game comment threads. As suggested by the name, a post-game thread is a comment thread posted after each game that allows for the expression of thoughts towards the teams or individual players performance. 

### Tools used:
* Languages: Python
* Packages: pandas, requests, re, ntlk, beautifulsoup4, praw

### Data Collection
