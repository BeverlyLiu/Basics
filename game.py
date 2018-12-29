game_size = 3
game = []
for i in range(game_size):
    row = []
    for i in range(game_size):
        row.append(0)
    game.append(row)

game1 = [[0 for i in range(game_size)] for i in range(game_size)]

print(game, '\n\n', game1)

