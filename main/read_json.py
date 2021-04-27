import json

with open('Players.json') as f:
    data = json.load(f)

for players in data['players']:
    print(players)