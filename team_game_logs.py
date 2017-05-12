from nba_py import team
from nba_py.constants import TEAMS
import json

team_list = team.TeamList().info() # retrieve list of dicts that stores team info

# store game logs for each team in json file
for t in team_list:

	if t['ABBREVIATION'] is None:
		continue

	filepath = "team_stats_2010/" + t['ABBREVIATION']+'.json'
	print(filepath)
	logs = None

	for year in range(2010, int(t['MAX_YEAR']) +1):
		next_year = str((year+1)%100)

		if len(next_year) == 1:
			next_year = '0'+next_year

		season = str(year) + '-' + next_year
		print(season)
		season_log = team.TeamGameLogs(t['TEAM_ID'], season=season).info()

		if not logs:
			logs = season_log
		else:
			logs += season_log

	with open(filepath, 'w') as f:
		json.dump(logs, f)