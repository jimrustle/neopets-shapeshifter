import copy

solution = []

# levels are defined as lists of rows,
# len(level) = number of rows (y-dimension)
# len(level[1]) = number of columns (x-dimension)
level = [[1, 0, 1], [1, 0, 1], [0, 0, 1]]

shapes = [[[0, 1, 1], [1, 1, 1]],
          [[1]],
          [[1,1], [1,1], [1,1]],
          [[1]],
          [[0,1], [1,1]],
          [[1], [1]],
          [[1, 0], [1,1], [1,0]],
          [[1], [1]]]

def pprint(board):
    for y in board:
        print(''.join(map(str, y)))
    print('---')


def apply_piece(shape, board, location):
    loc_x = location[0]
    loc_y = location[1]
    for (i, row) in enumerate(shape):
        for (j, column) in enumerate(row):
            board[loc_y + i][loc_x + j] ^= column

def placeable(shape, board, location):
    # shapes must be placed to fit the board,
    # ie. cannot fit where their protrusions may exit the board
    board_x = len(board[0])
    board_y = len(board)
    loc_x = location[0]
    loc_y = location[1]
    shape_x = len(shape[0])
    shape_y = len(shape)
    return (loc_x + shape_x <= board_x) and (loc_y + shape_y <= board_y)

def bt(board, pieces):
    # if board is all 0 and no pieces are left, it is solved
    if sum(map(sum, board)) == len(board)**2 and len(pieces) == 0:
        # print("solution found")
        return True
    if len(pieces) == 0:
        return False
    for x in range(len(board[1])):
        for y in range(len(board)):
            if placeable(pieces[0], board, (x, y)):
                solution.append((x,y))

                saved = copy.deepcopy(board)
                apply_piece(pieces[0], board, (x, y))

                if bt(board, pieces[1:]):
                    return True

                solution.pop()
                board = copy.deepcopy(saved)
    return False

# test apply
# print("level:")
# pprint(level)
# s = shapes
# apply_piece(s[0], level, (0, 0))
# pprint(level)
# apply_piece(s[1], level, (0, 0))
# pprint(level)
# apply_piece(s[2], level, (0, 0))
# pprint(level)
# apply_piece(s[3], level, (0, 0))
# pprint(level)
# apply_piece(s[4], level, (0, 1))
# pprint(level)
# apply_piece(s[5], level, (0, 1))
# pprint(level)

bt(level, shapes)
print(solution)

