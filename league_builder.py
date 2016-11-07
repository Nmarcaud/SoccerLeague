# Script Soccer League v1

import csv
import random

Sharks = []
Dragons = []
Raptors = []

player_hight_xp = []
player_low_xp = []

# Importation
with open('soccer_players.csv') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=',', quotechar='|')
    players = list(reader)
    for player in players:
        
        # isole dans une liste (player_hight_xp) ceux qui ont de l'xp 
        if player['Soccer Experience'] == 'YES':
            player_hight_xp.append(player)
            
        # isole dans une liste (player_low_xp) ceux qui n'ont pas d'xp
        else:
            player_low_xp.append(player)


# répartir les bons et les moins bons dans les teams

for player in player_hight_xp:
    while player in Sharks or player in Dragons or player in Raptors:
        continue
    else:
        if len(Sharks) < 3:
            Sharks.append(player)
            
        elif len(Dragons) < 3:
            Dragons.append(player)
            
        else:
            Raptors.append(player)
        
for player in player_low_xp:
    while player in Sharks or player in Dragons or player in Raptors:
        continue
    else:
        if len(Sharks) < 6:
            Sharks.append(player)

        elif len(Dragons) < 6:          
            Dragons.append(player)
            
        else:
            Raptors.append(player)

# exportation dans un fichier txt
results = open("teams.txt", "w")

results.write('Sharks\n')
for player in Sharks:
    results.write(', '.join([player['Name'], player['Soccer Experience'], player['Guardian Name(s)']]))
    results.write('\n')
results.write('\n')

results.write('Dragons\n')
for player in Dragons:
    results.write(', '.join([player['Name'], player['Soccer Experience'], player['Guardian Name(s)']]))       
    results.write('\n')
results.write('\n')

results.write('Raptors\n')
for player in Raptors:
    results.write(', '.join([player['Name'], player['Soccer Experience'], player['Guardian Name(s)']]))       
    results.write('\n')
results.write('\n')

results = open("teams.txt", "r")

