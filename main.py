#create virtual environment
#cd *whatever folder your working in*
#python -m venv .venv
#pip install everything you need

#use virtual environment
#source .venv/bin/activate
#deactivate

#streamlit run file.py

#from nba_api.stats.endpoints import commonplayerinfo
#from nba_api.stats.endpoints import playerheadlinestats
import pandas as pd
import numpy as np
from nba_api.stats.static import players
from nba_api.stats.endpoints import playercareerstats
import nba_api.stats.endpoints as endpoints
from nba_api.stats.endpoints import leaguedashplayerstats

# Define the season
season = '2021-22'  # Replace with the season you're interested in

# Access the LeagueDashPlayerStats endpoint
player_stats = leaguedashplayerstats.LeagueDashPlayerStats(season=season)

# Convert data to a Pandas DataFrame
stats_df = player_stats.get_data_frames()[0]

stats_df['PTS_PER_GAME'] = stats_df['PTS'] / stats_df['GP']

# Sorting the DataFrame by Points Per Game in descending order
sorted_df = stats_df.sort_values(by='PTS_PER_GAME', ascending=False)

# Displaying the sorted DataFrame
print(sorted_df[['PLAYER_NAME', 'PTS_PER_GAME']])

# To see all available modules and classes in 'endpoints'
#print(dir(endpoints))

#player_info = commonplayerinfo.PlayerHeadlineStats(player_id=203999)
#print(player_info.get_data_frames()[0])

#x = players.get_players() #gives player ID, full name, first name, last name, active/inactive
#for player in x:
    #career = playercareerstats.PlayerCareerStats(player_id = player['id'])
    #print(career.get_data_frames()[0])
    #break



# How to get data for one player: Nikola Jokić
#career = playercareerstats.PlayerCareerStats(player_id='203999') 

#career.get_data_frames()[0]
