import random

def chunks(l, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(l), n):
        yield l[i:i + n]

def generate_tiles(n_tiles):
    return sorted(set([random.randint(0, n_tiles - 1) for i in range(n_tiles)]))

def tile_width(tile, board_size):
    return max(map(lambda  x: (x % board_size) + 1, tile))

def allowable_pos(tile_width, position, board_size):
    return tile_width < (board_size - position % board_size) + 1

# define tiles
tiles = [[0, 1, 2],
        [0, 1, 6, 7],
        [0, 1, 2, 7],
        [1, 6, 7, 8, 13],
        [0, 1, 6, 12],
        [0, 6, 7, 8, 9]]

#tiles = [generate_tiles(10) for i in range(6)]

# define board size
board_size = 6
nstates = 2

# apply tiles to board
board = [1 for i in range(board_size**2)]

for tile in tiles:
    position = random.randint(0, board_size**2 - 1 - tile[-1])
    while not(allowable_pos(tile_width(tile, board_size), position, board_size)):
        position = random.randint(0, board_size**2 - 1 - tile[-1])

    #print(position)
    for idx in tile:
        board[position + idx] += 1
        board[position + idx] %= nstates

# print output
#print('-----')
print(board_size, board_size)
for row in chunks(board, board_size):
    print(" ".join(str(c) for c in row))
print("1")
print(len(tiles))
for tile in tiles:
    print(len(tile), " ".join(str(c) for c in tile))
