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
shark_count = 0
dragon_count = 0
raptor_count = 0

for player in player_hight_xp:
    if shark_count < 3:
        if player in Sharks or player in Dragons or player in Raptors:
            continue
        else:
            Sharks.append(player)
            shark_count += 1
            continue
    elif dragon_count < 3:
        if player in Sharks or player in Dragons or player in Raptors:
            continue
        else:
            Dragons.append(player)
            dragon_count += 1
            continue
    elif raptor_count < 3:
        if player in Sharks or player in Dragons or player in Raptors:
            continue
        else:
            Raptors.append(player)
            raptor_count += 1
            continue
        
for player in player_low_xp:
    if shark_count < 6:
        if player in Sharks or player in Dragons or player in Raptors:
            continue
        else:
            Sharks.append(player)
            shark_count += 1
            continue
    elif dragon_count < 6:
        if player in Sharks or player in Dragons or player in Raptors:
            continue
        else:
            Dragons.append(player)
            dragon_count += 1
            continue
    elif raptor_count < 6:
        if player in Sharks or player in Dragons or player in Raptors:
            continue
        else:
            Raptors.append(player)
            raptor_count += 1
            continue

# ok exporter en fichier texte

print('Sharks')
for player in Sharks:
    print(', '.join([player['Name'], player['Soccer Experience'], player['Guardian Name(s)']]))
    
print('')

print('Dragons')
for player in Sharks:
    print(', '.join([player['Name'], player['Soccer Experience'], player['Guardian Name(s)']]))
    
print('')

print('Raptors')
for player in Sharks:
    print(', '.join([player['Name'], player['Soccer Experience'], player['Guardian Name(s)']]))
    
print('')
    


    
# exportation dans un fichier txt
