# write a function that accepts two arrays of players and
# returns an array of the players who play in both sports; the
# algo needs to be O(M+N)

basketball_players = [
    {"first_name": "Jill",  "last_name": "Huang",    "team": "Gators"},
    {"first_name": "Janko", "last_name": "Barton",   "team": "Sharks"},
    {"first_name": "Wanda", "last_name": "Vakulskas","team": "Sharks"},
    {"first_name": "Jill",  "last_name": "Moloney",  "team": "Gators"},
    {"first_name": "Luuk",  "last_name": "Watkins",  "team": "Gators"}
    ]

football_players = [
    {"first_name":"Hanzla", "last_name":"Radosti","team": "32ers"},
    {"first_name":"Tina", "last_name":"Watkins","team":"Barleycorns"},
    {"first_name":"Alex", "last_name":"Patel","team":"32ers"},
    {"first_name":"Jill",  "last_name":"Huang","team":"Barleycons"},
    {"first_name":"Wanda","last_name":"Vakulskas", "team":"Barleycorns"}
    ]

def plays_both_sports(players1,players2):
    hash1 = {}
    for table in players1:
        full_name = table["first_name"]+" "+ \
                    table["last_name"]
        hash1.update({full_name:True})
 
    player_list = [] 
    for table in players2:
        full_name = table["first_name"]+" "+ \
                    table["last_name"]
        if hash1.get(full_name)==True:
            player_list.append(full_name)

    return player_list

print(plays_both_sports(basketball_players,football_players))
