import pandas as pd
import soccerdata as sd
import sys
idx = int(sys.argv[1])
print('My idx:', idx)

ids = pd.read_csv('premier_league_2021_whoscore_ids.csv')

matches_subset = ids.game_id_x.tolist()[idx*95:(idx+1)*95]
ws = sd.WhoScored('ENG-Premier League', seasons=2021, no_cache=False)
ws.read_events(match_id = matches_subset, output_fmt=None)

