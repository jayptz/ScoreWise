from nba_api.stats.endpoints import playercareerstats
from nba_api.stats.static import players

# Nikola Jokić
career = playercareerstats.PlayerCareerStats(player_id='203999') 

# pandas data frames (optional: pip install pandas)
career.get_data_frames()[0]

# json
career.get_json()

# dictionary
career.get_dict()

def get_active_players():
    active_players = [player for player in players.get_players() if player['is_active']]
    return active_players

active_players = get_active_players()
print(active_players[:5])







