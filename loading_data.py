import soccerdata as sd

fbref = sd.FBref(data_dir="/tmp", no_cache=False, no_store=True, leagues="ENG-Premier League", seasons=2021)

player_match_stats = fbref.read_player_match_stats(stat_type="passing", match_id='db261cb0')
player_match_stats.head()
