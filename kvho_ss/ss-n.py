import copy
import numpy as np

import cProfile

def read_level(filename):
    game = {}
    with open(filename, 'r') as f:
        level = f.read().split('\n')
        game['x'] = int(level[0].split(' ')[0])
        game['y'] = int(level[0].split(' ')[1])

        board = []
        for i in range(1, game['y'] + 1):
            for v in map(int, level[i].split(' ')):
                board.append(v)
        game['board'] = np.array(board)
        game['goal'] = int(level[game['y'] + 1])
        game['n_pieces'] = int(level[game['y'] + 2])

        pieces = []
        p_x = []
        p_y = []
        # p_t = []
        for i in range(game['y'] + 3, len(level) - 1):
            piece = list(map(int, level[i].split(' ')[1:]))
            pieces.append(np.array(piece))
            p_x.append(max(map(lambda x: x % game['x'], piece)) + 1)
            p_y.append(max(piece) // game['x'] + 1)
            # p_t.append(int(level[i].split(' ')[0]))

        game['pieces'] = pieces
        game['p_x'] = np.array(p_x)
        game['p_y'] = np.array(p_y)

        game['p'] = list(zip(pieces, p_x, p_y))

    return game

def apply_piece(piece, board, position):
    nstates = 2
    board[position + piece] += 1
    board[position + piece] %= nstates

def max_moves(game):
    moves = 1
    for i in range(len(game['pieces'])):
        moves *= (game['x'] - game['p_x'][i] + 1) * (game['y'] - game['p_y'][i] + 1)
    return moves

def placeable(piece_w, piece_l, game, position):
    return (piece_w < (game['x'] - position % game['x']) + 1) and (piece_l < game['y'] - (position // game['x']) + 1)

def solve(game):
    solution = []
    def bt(game, board, p):
        # if board is all 0 and no pieces are left, it is solved
        if sum(board) == game['x'] * game['y'] * game['goal'] and len(p) == 0:
            return True
        if len(p) == 0:
            return False
        for (piece, pw, pl) in p:
            for position in range(game['x'] * game['y']):
                if placeable(pw, pl, game, position):
                    solution.append(position)

                    apply_piece(piece, board, position)

                    if bt(game, board, p[1:]):
                        return True

                    solution.pop()
                    apply_piece(piece, board, position)
        return False
    if bt(game, game['board'], game['p']):
        return solution
    else:
        print("no solution")
        return False

def main():
    game = read_level('saved3')
    print(solve(game))

if __name__ == "__main__":
    main()
    # cProfile.run('main()')

