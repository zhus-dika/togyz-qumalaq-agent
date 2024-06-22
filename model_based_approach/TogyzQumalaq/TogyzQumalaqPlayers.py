import numpy as np

"""
Random and Human-ineracting players for the game of TicTacToe.

Author: Evgeny Tyurin, github.com/evg-tyurin
Date: Jan 5, 2018.

Based on the OthelloPlayers by Surag Nair.

"""
class RandomPlayer():
    def __init__(self, game):
        self.game = game

    def play(self, board):
        val_moves = self.game.getValidMoves(board, 1)
        move = np.random.choice(np.nonzero(val_moves)[0], 1)[0]
        return move


class HumanTogyzQumalaqPlayer():
    def __init__(self, game, n_x, n_y):
        self.game = game
        self.n_x = n_x
        self.n_y = n_y

    def play(self, board):
        valid_moves = self.game.getValidMoves(board, 1)
        print(valid_moves)

        while True:
            # Python 3.x
            a = input()
            # Python 2.x
            # a = raw_input()
            if a in valid_moves:
                break
            else:
                print('Invalid move')
        return a