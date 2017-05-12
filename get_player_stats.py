from nba_py import player
import pandas
import nba_py
import json


player_list = player.PlayerList(season='2016-17').info()
list_id = player_list['PERSON_ID']
df = pandas.DataFrame()

for id in list_id:
	print(id)
	season_totals = player.PlayerCareer(id).regular_season_totals()
	player_season = season_totals.loc[season_totals['SEASON_ID']=='2016-17']
	df = df.append(player_season, ignore_index=True)

print(df)
df.to_pickle('16-17allplayers_totals')