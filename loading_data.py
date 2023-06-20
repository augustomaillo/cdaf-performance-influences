import soccerdata as sd

fbref = sd.FBref(leagues="ENG-Premier League", seasons=2021, no_cache=False)

player_match_stats = fbref.read_player_match_stats(stat_type="passing", match_id='db261cb0')

print(player_match_stats.head())
