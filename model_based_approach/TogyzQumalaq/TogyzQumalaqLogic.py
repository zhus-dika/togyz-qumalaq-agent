from utils import *
import numpy as np
'''
Board class for the game of TicTacToe.
Default board size is 3x3.
Board data:
  1=white(O), -1=black(X), 0=empty
  first dim is column , 2nd is row:
     pieces[0][0] is the top left square,
     pieces[2][0] is the bottom left square,
Squares are stored and manipulated as (x,y) tuples.

Author: Evgeny Tyurin, github.com/evg-tyurin
Date: Jan 5, 2018.

Based on the board for the game of Othello by Eric P. Nichols.

'''
# from bkcharts.attributes import color

class Board():

    def __init__(self, n_x=10, n_y=32):
        "Set up initial board configuration."
        self.players = [1, -1]
        self.n_x = n_x
        self.n_y = n_y
        # Create the empty board array.
        self.pieces = np.zeros((n_x, n_y))
        # Set up the initial 18 pieces.
        for i in range(1, n_x):
            for j in range(9):
                self.pieces[i][j] = 1
                self.pieces[i][n_y - 1 - j] = -1

    # add [][] indexer syntax to the Board
    def __getitem__(self, index): 
        return self.pieces[index]

    def get_legal_moves(self, color):
        """Returns all the legal moves for the given color.
        (1 for white, -1 for black)
        @param color not used and came from previous version.        
        """

        moves = []  # stores the legal moves.

        # Get all the empty squares (color==0)
        for x in range(1, self.n_x):
            if color > 0 and self.pieces[x][0] > 0:
                moves.append(x - 1)
            elif color < 0 and self.pieces[x][self.n_y - 1] < 0:
                moves.append(x - 1)
        return moves

    def has_legal_moves(self, player):
        # env = convertBoard2TogyzQumalaq(self.pieces, 1)
        # cur_player = env.possible_agents.index(env.agent_selection)
        # player = 1 - 2 * cur_player
        if len(self.get_legal_moves(player)) > 0:
            return True
        return False
    
    def is_win(self, color):
        """Check whether the given player has collected a triplet in any direction;
        @param color (1=white,-1=black)y
        """
        env = convertBoard2TogyzQumalaq(self.pieces, color)
        cur_player = int((1 - color) / 2)
        opp_player = int((cur_player + 1) % 2)
        if env.qazandar[cur_player] > 81:
            return True
        if (env.check_atsyrau(env.possible_agents[opp_player])
                and env.qazandar[opp_player] < 81):
            return True
        return False
        # cnt = 0
        # if color > 0:
        #     for j in range(self.n_y - 1):
        #         if self.pieces[0][j] > 0:
        #             cnt += 1
        #     if cnt > 81:
        #         return True
        # else:
        #     for j in range(self.n_y - 1):
        #         if self.pieces[0][self.n_y - 1 - j] < 0:
        #             cnt += 1
        #     if cnt > 81:
        #         return True
        # return False


    def calculate_qumalaqs(self):
        n_x = self.pieces.shape[0]
        n_y = self.pieces.shape[1]
        cnt = {1: [], -1: []}
        for i in range(n_x):
            cnt_loc1 = 0
            cnt_loc2 = 0
            for j in range(n_y):
                if self.pieces[i][j] > 0 and j != n_y - 1:
                    cnt_loc1 += self.pieces[i][j]
                elif self.pieces[i][j] < 0 and j != 0:
                    cnt_loc2 += - self.pieces[i][j]
            cnt[1].append(cnt_loc1)
            cnt[-1].append(cnt_loc2)
        cnt_full = sum(cnt[1] + cnt[-1])
        return cnt_full

    def execute_move(self, move, player):
        """Perform the given move on the board; 
        color gives the color pf the piece to play (1=white,-1=black)
        """
        env = convertBoard2TogyzQumalaq(self.pieces, player)
        env.step(move)
        self.pieces = convertTogyzQumalaq2Board(env)