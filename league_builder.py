# Script Soccer League v2

import csv

Sharks = []
Dragons = []
Raptors = []

# (main)
def program():
    
    # Importation
    with open('soccer_players.csv') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',', quotechar='|')
        players = list(reader)
        for player in players:
            
            # isole et réparti ceux qui ont de l'xp 
            if player['Soccer Experience'] == 'YES':
                while player in Sharks or player in Dragons or player in Raptors:
                    continue
                else:
                    if len(Sharks) < 3:
                        Sharks.append(player)
                
                    elif len(Dragons) < 3:
                        Dragons.append(player)
                
                    else:
                        Raptors.append(player)
                
            # isole et réparti dans une liste ceux qui n'ont pas d'xp
            else:
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

# eviter l'importation auto (se lance à la commande program() )
if __name__ == '__program__':
    program()

