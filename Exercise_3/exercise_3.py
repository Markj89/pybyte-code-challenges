games_won = dict(sara=0, bob=1, tim=5, julian=3, jim=1)

def print_game_stats(games_won=games_won):
    for winner, game in games_won.items():
        print(winner, ' has won ', game, format('game' if game == 1 else 'games'))
        
print_game_stats()
