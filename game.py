player = {'name': 'Manuel', 'attack': 13, 'heal': 16, 'health': 100}
monster = {'name': 'Max', "attack": 12, 'health': 100}
game_running = True

while game_running == True:

    print('Please select action')
    print('1) Attack')
    print('2) Heal')

    player_choice = input()

    if player_choice == "1":
        monster['health'] = monster['health'] - player['attack']
        player['health'] = player['health'] - monster['attack']

        print(monster['health'])
        print(player['health'])
        
    elif player_choice == '2':
        print('Heal Player')

    if player['health'] <= 0 or monster['health'] <= 0:
        game_running = False
