from __future__ import print_function
import sys
sys.path.append('..')
from Game import Game
from TogyzQumalaq.TogyzQumalaqLogic import Board
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go

class TogyzQumalaqGame(Game):
    square_content = {
        -1: "x",
        +0: "-",
        +1: "o",
        -10: "X",
        +10: "O"
    }

    @staticmethod
    def getSquarePiece(piece):
        return TogyzQumalaqGame.square_content[piece]

    def __init__(self, n_x, n_y):
        self.n_x = n_x
        self.n_y = n_y

    def getInitBoard(self):
        # return initial board (numpy board)
        b = Board(self.n_x, self.n_y)
        return np.array(b.pieces)

    def getBoardSize(self):
        # (a,b) tuple
        return (self.n_x, self.n_y)

    def getActionSize(self):
        # return number of actions
        return 9

    def getNextState(self, board, player, action):
        # if player takes action on board, return next (board,player)
        # action must be a valid move
        # if action == self.n * self.n * self.n:
        #     return (board, -player)
        b = Board(self.n_x, self.n_y)
        b.pieces = np.copy(board)
        b.execute_move(action, player)
        #player_name = 'Bastaushy' if player == 1 else 'Qostaushy'
        #print(f'{player_name} makes action {action + 1}')
        #print('player from getNextState', player)
        return (b.pieces, -player)

    def getValidMoves(self, board, player):
        # return a fixed size binary vector
        valids = [0] * self.getActionSize()
        b = Board(self.n_x, self.n_y)
        b.pieces = np.copy(board)
        legalMoves = b.get_legal_moves(player)
        # if len(legalMoves) == 0:
        #     valids[-1] = 1
        #     return np.array(valids)
        for i in legalMoves:
            valids[i] = 1
        return np.array(valids)

    def getGameEnded(self, board, player):
        # return 0 if not ended, 1 if player 1 won, -1 if player 1 lost
        # player = 1
        b = Board(self.n_x, self.n_y)
        b.pieces = np.copy(board)

        if b.is_win(player):
            return player
        if b.is_win(-player):
            return -player
        if b.has_legal_moves(player):
            return 0
        # draw has a very little value
        return 1e-04

    def getCanonicalForm(self, board, player):
        # return state if player==1, else return -state if player==-1
        return player * board[:, ::player]


    def getSymmetries(self, board, pi):
        """
        Полностью отражает доску тогызкумалақ относительно центральной вертикальной оси.

        Args:
            board (np.array): Игровая доска (10×162).
            pi (list): Политика (распределение вероятностей ходов), длина 9.

        Returns:
            list: [(отраженная доска, `pi`)]
        """
        l = [(board, pi)]  # Добавляем оригинальную доску

        # Полностью отражаем доску по вертикальной оси
        # mirrored_board = np.fliplr(board) * -1

        # pi не изменяется
        # l.append((mirrored_board, pi))

        return l

    def stringRepresentation(self, board):
        # numpy array (canonical board)
        return board.tobytes()

    @staticmethod
    def render(board, mode='plt'):
        n_x = board.n_x
        n_y = board.n_y
        x0_points = []
        y0_points = []

        x1_points = []
        y1_points = []
        for x in range(n_x):
            for y in range(n_y):
                if board.pieces[x][y] > 0:
                    x0_points.append(x)
                    y0_points.append(y)
                # ===========================
                if board.pieces[x][y] < 0:
                    x1_points.append(x)
                    y1_points.append(y)
        if mode== 'plt':
            fig = plt.figure(figsize=(10,6))
            ax = fig.add_subplot()
            ax.set_title(f'Render game board')
            ax.scatter(x0_points, y0_points, s=2, label='Bastaushy points')
            ax.scatter(x1_points, y1_points, s=2, label='Qostaushy points')
            ax.legend()


    @staticmethod
    def display_board(board):
        n_x = board.shape[0]
        n_y = board.shape[1]
        for _ in range(n_y + 12):
            print('=', end="")
        cnt = {1: [], -1: []}
        for i in range(n_x):
            cnt_loc1 = 0
            cnt_loc2 = 0
            for j in range(n_y):
                if board[i][j] > 0 and j != n_y - 1:
                    cnt_loc1 += board[i][j]
                elif board[i][j] < 0 and j != 0:
                    cnt_loc2 += - board[i][j]
            cnt[1].append(cnt_loc1)
            cnt[-1].append(cnt_loc2)
        print("")
        for i in range(n_x):
            cnt_str = str(int(cnt[1][i]))
            service_str = ''
            for _ in range(3 - len(cnt_str)):
                service_str += '0'
            print(service_str + cnt_str + '|', end="")
            print(str(i) + '|', end="")
            for j in range(n_y):
                if board[i][j] != 0:
                    print(TogyzQumalaqGame.square_content[board[i][j]], end="")
                else:
                    print('-', end="")
            cnt_str = str(int(cnt[-1][i]))
            service_str = ''
            for _ in range(3 - len(cnt_str)):
                service_str += '0'
            print('|' + str(i), end="")
            print('|' + service_str + cnt_str, end="")
            print("")
        for _ in range(n_y + 12):
            print('=', end="")
        print("")
        cnt_full = sum(cnt[1] + cnt[-1])
        print(f'Full board stones: {cnt_full}')
    # @staticmethod
    # def display(board):
    #     n = board.shape[0]
    #
    #     print("   ", end="")
    #     for y in range(n):
    #         print(y, "", end="")
    #     print("")
    #     print("  ", end="")
    #     for _ in range(n):
    #         print("-", end="-")
    #     print("--")
    #     for y in range(n):
    #         print(y, "|", end="")  # print the row #
    #         for x in range(n):
    #             piece = board[y][x]  # get the piece to print
    #             if piece == -1:
    #                 print("X ", end="")
    #             elif piece == 1:
    #                 print("O ", end="")
    #             else:
    #                 if x == n:
    #                     print("-", end="")
    #                 else:
    #                     print("- ", end="")
    #         print("|")
    #
    #     print("  ", end="")
    #     for _ in range(n):
    #         print("-", end="-")
    #     print("--")