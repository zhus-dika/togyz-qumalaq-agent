import sys
import unittest
sys.path.append('./')
from model_based_approach.utils import *
from model_based_approach.TogyzQumalaq.TogyzQumalaqLogic import Board
from model_based_approach.TogyzQumalaq.TogyzQumalaqGame import TogyzQumalaqGame


class TestListElements(unittest.TestCase):
    def test_states(self):
        #============================================
        # TEST #1
        game = TogyzQumalaqGame(10, 32)
        board = Board()
        moves = {1: [], -1: []}
        player = 1
        acts = [4, 5, 8, 0, 5, 7, 5, 3, 7, 5, 2, 7, 5, 8, 6, 4, 8, 4, 3, 5]
        MOVES = {
            1: [acts[i] for i in range(len(acts)) if i%2 == 0],
            -1: [acts[i] for i in range(len(acts)) if i%2 == 1]
        }
        game.display_board(board.pieces)
        j = 0
        for i in range(len(acts)):
            move = MOVES[player][j]
            if i % 2 == 1:
                j += 1
            moves[player].append(move)
            pieces, player = game.getNextState(board.pieces, player, move)
            board.pieces = pieces
            game.display_board(board.pieces)
            if game.getGameEnded(board.pieces, player) != 0:
                break
        env = convertBoard2TogyzQumalaq(board.pieces, player)
        tuzdyq_test = [12, -1]
        otaular_test = [17, 0, 4, 1, 5, 4, 3, 6, 2, 10, 20, 19, 0, 2, 1, 19, 5, 1]
        qazandar_test = [25, 18]

        self.assertEqual(env.otaular, otaular_test)
        self.assertEqual(env.tuzdyq, tuzdyq_test)
        self.assertEqual(env.qazandar, qazandar_test)
        #============================================
        # TEST #2
        game = TogyzQumalaqGame(10, 32)
        board = Board()
        moves = {1: [], -1: []}
        player = 1
        acts = [4, 7, 0, 6, 3, 3, 1, 0, 6, 3]
        MOVES = {
            1: [acts[i] for i in range(len(acts)) if i%2 == 0],
            -1: [acts[i] for i in range(len(acts)) if i%2 == 1]
        }
        game.display_board(board.pieces)
        j = 0
        for i in range(len(acts)):
            move = MOVES[player][j]
            if i % 2 != 0:
                j += 1
            moves[player].append(move)
            pieces, player = game.getNextState(board.pieces, player, move)
            board.pieces = pieces
            game.display_board(board.pieces)
            if game.getGameEnded(board.pieces, player) != 0:
                break
        tuzdyq_test = [-1, 3]
        otaular_test = [4, 3, 14, 0, 6, 15, 1, 14, 14, 2, 14, 14, 1, 14, 3, 3, 4, 13]
        qazandar_test = [20, 3]

        env = convertBoard2TogyzQumalaq(board.pieces, player)
        self.assertEqual(env.otaular, otaular_test)
        self.assertEqual(env.tuzdyq, tuzdyq_test)
        self.assertEqual(env.qazandar, qazandar_test)

        #============================================
        # TEST #3
        game = TogyzQumalaqGame(10, 32)
        board = Board()
        moves = {1: [], -1: []}
        player = 1
        acts = [2, 3, 8, 6, 4, 7, 0, 4, 3, 0, 1, 3, 8, 3, 7, 2, 2, 0, 6, 5, 7, 8]
        MOVES = {
            1: [acts[i] for i in range(len(acts)) if i%2 == 0],
            -1: [acts[i] for i in range(len(acts)) if i%2 == 1]
        }
        game.display_board(board.pieces)
        j = 0
        for i in range(len(acts)):
            move = MOVES[player][j]
            if i % 2 != 0:
                j += 1
            moves[player].append(move)
            pieces, player = game.getNextState(board.pieces, player, move)
            board.pieces = pieces
            game.display_board(board.pieces)
            if game.getGameEnded(board.pieces, player) != 0:
                break

        tuzdyq_test = [16, -1]
        otaular_test = [7, 5, 4, 8, 11, 21, 2, 2, 6, 4, 11, 4, 6, 5, 2, 11, 0, 2]
        qazandar_test = [49, 2]

        env = convertBoard2TogyzQumalaq(board.pieces, player)
        self.assertEqual(env.otaular, otaular_test)
        self.assertEqual(env.tuzdyq, tuzdyq_test)
        self.assertEqual(env.qazandar, qazandar_test)

    def test_check_tuzdyq(self):

        # ============================================
        # TEST #1
        game = TogyzQumalaqGame(10, 32)
        board = Board()
        moves = {1: [], -1: []}
        player = 1
        acts = [3, 8, 0, 8, 5, 6, 1, 1, 8, 5, 1, 7, 5, 0, 6, 1, 2, 5, 1, 8]
        MOVES = {
            1: [acts[i] for i in range(len(acts)) if i % 2 == 0],
            -1: [acts[i] for i in range(len(acts)) if i % 2 == 1]
        }
        game.display_board(board.pieces)
        j = 0
        for i in range(len(acts)):
            move = MOVES[player][j]
            if i % 2 != 0:
                j += 1
            moves[player].append(move)
            pieces, player = game.getNextState(board.pieces, player, move)
            board.pieces = pieces
            game.display_board(board.pieces)
            if game.getGameEnded(board.pieces, player) != 0:
                break

        env = convertBoard2TogyzQumalaq(board.pieces, player)
        tuzdyq_test = [-1, 5]
        self.assertEqual(env.tuzdyq, tuzdyq_test)

        # ============================================
        # TEST #2
        game = TogyzQumalaqGame(10, 32)
        board = Board()
        moves = {1: [], -1: []}
        player = 1
        acts = [7,7,1,0,4,4,3,7,1,8,0]
        MOVES = {
            1: [acts[i] for i in range(len(acts)) if i % 2 == 0],
            -1: [acts[i] for i in range(len(acts)) if i % 2 == 1]
        }
        game.display_board(board.pieces)
        j = 0
        for i in range(len(acts)):
            move = MOVES[player][j]
            if i % 2 != 0:
                j += 1
            moves[player].append(move)
            pieces, player = game.getNextState(board.pieces, player, move)
            board.pieces = pieces
            game.display_board(board.pieces)
            if game.getGameEnded(board.pieces, player) != 0:
                break

        env = convertBoard2TogyzQumalaq(board.pieces, player)
        tuzdyq_test = [13, 6]
        self.assertEqual(env.tuzdyq, tuzdyq_test)

    def test_check_atsyrau(self):
        ### Test #1
        acts = [6,2,5,8,3,0,8,4,1,5,
        	3,2,3,0,7,1,4,7,1,0,
        	0,5,6,3,0,3,3,1,7,4,
        	8,0,4,1,6,2,4,1,2,8,
        	6,8,6,7,2,4,4,1,6,7,
        	8,6,4,1,8,8,8,5,7,2,
        	3,2,2,4,0,1,6,0,8,1,
        	0,4,4,8,8,1,2,8,7,2,
        	8,2,5,4,4,8,6,4,2,1,
        	7,0,5,5,6,8,2,2,2,1,
        	8,6,8,8,4,0,7,2,5,2,
        	2,1,8,7,0,0,6,6,8,0,
        	6,7,5,2,3,0,2,2,7,2,
        	6,5,8,6,6,1,8,0,4,5,
        	4,5,5,6,6,2,5,4,6,5,
        	3,1,4,1,5,2,7,6,8,0,
        	7,0,3,4,4,6,6,5,5,1,
        	6,1,7,6,7,2,8,5,8,8,
        	0,8,0,2]
        game = TogyzQumalaqGame(10, 32)
        board = Board()
        moves = {1: [], -1: []}
        player = 1
        MOVES = {
            1: [acts[i] for i in range(len(acts)) if i % 2 == 0],
            -1: [acts[i] for i in range(len(acts)) if i % 2 == 1]
        }
        game.display_board(board.pieces)
        j = 0
        for i in range(len(acts)):
            move = MOVES[player][j]
            if i % 2 != 0:
                j += 1
            moves[player].append(move)
            pieces, player = game.getNextState(board.pieces, player, move)
            board.pieces = pieces
            game.display_board(board.pieces)
            if game.getGameEnded(board.pieces, player) != 0:
                break
        self.assertTrue(board.is_win(player))

    def test_check_for_winner(self):
        ### Test #1
        acts = [4, 8, 7, 4, 8, 2, 5, 7, 7, 0,
                7, 1, 2, 5, 6, 7, 0, 8, 1, 8,
                5, 0, 1, 1, 8, 0, 6, 0, 3, 3,
                3, 0, 6, 6, 7, 4, 8, 2, 2, 3,
                1, 8, 6, 8, 6, 1, 0, 3, 1, 1,
                5, 2, 7, 6, 1, 1, 7, 8, 0, 2,
                6, 7, 5, 7, 2, 8, 1, 3, 2, 3,
                7, 6, 5, 4, 7, 5, 6, 8, 0, 7,
                5, 8, 7, 4, 2, 5, 7, 1, 6, 2,
                6, 1, 8, 6, 8, 8, 7, 2, 8, 7,
                3, 2, 5, 3, 3, 4, 6, 4, 0, 5,
                7, 3, 2, 5, 3, 1, 2, 6, 8, 6,
                7, 4, 0, 2, 3, 3, 8, 7, 0, 8,
                6, 4, 1, 5, 0, 6, 7, 5, 8, 8,
                0, 6, 2, 7, 2, 7, 0, 8, 1, 8]
        game = TogyzQumalaqGame(10, 32)
        board = Board()
        moves = {1: [], -1: []}
        player = 1
        MOVES = {
            1: [acts[i] for i in range(len(acts)) if i % 2 == 0],
            -1: [acts[i] for i in range(len(acts)) if i % 2 == 1]
        }
        game.display_board(board.pieces)
        j = 0
        for i in range(len(acts)):
            move = MOVES[player][j]
            if i % 2 != 0:
                j += 1
            moves[player].append(move)
            pieces, player = game.getNextState(board.pieces, player, move)
            board.pieces = pieces
            game.display_board(board.pieces)
            if game.getGameEnded(board.pieces, player) != 0:
                break

        self.assertTrue(board.is_win(player))
if __name__ == "__main__":
    unittest.main()