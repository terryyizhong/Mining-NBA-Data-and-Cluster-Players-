from nba_py import player
from nba_py.player import get_player
import json

mvp_name =[("James", "Harden"), ("Russell", "Westbrook"), ("Lebron", "James"), 
            ("Kawhi", "Leonard"), ("Isaiah", "Thomas"), ("John", "Wall"), 
            ("Kevin", "Durant"), ("Stephen", "Curry"), ("Chris", "Paul"),
            ("DeMar", "DeRozan")]
mvp_id = []
for name in mvp_name:
    first, last = name
    mvp_id.append(get_player(first, last_name=last))

print(mvp_id)
logs = None
for id in mvp_id:
    player_gamelog = player.PlayerGameLogs(id).info()
    if not logs:
        logs = player_gamelog
    else:
        logs += player_gamelog
print(logs)
with open('mvp_game.json', 'w') as f:
    json.dump(logs, f)


# players = player.PlayerList().info()
# print players