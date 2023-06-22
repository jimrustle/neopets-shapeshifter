import random

def chunks(l, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(l), n):
        yield l[i:i + n]

# define tiles
tiles = [[0, 1, 2],
         [0, 1, 6, 7],
         [0, 1, 2, 7],
         [1, 6, 7, 8, 13],
         [0, 1, 6, 12],
         [0, 6, 7, 8]]

# define board size
board_size = 6
nstates = 2

# apply tiles to board
board = [1 for i in range(6**2)]

for tile in tiles:
    position = random.randint(0, board_size**2 - 1 - tile[-1])
    print(position)
    for idx in tile:
        board[position + idx] += 1
        board[position + idx] %= nstates

# print output
print('-----')
print(board_size, board_size)
for row in chunks(board, 6):
    print(" ".join(str(c) for c in row))
print("1")
print(len(tiles))
for tile in tiles:
    print(len(tile), " ".join(str(c) for c in tile))
