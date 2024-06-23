import sys
import unittest
sys.path.append('model_based_approach')
from utils import *
from TogyzQumalaq.TogyzQumalaqLogic import Board
from TogyzQumalaq.TogyzQumalaqGame import TogyzQumalaqGame

MOVES = {
    1: [3,8,3,2,1,2,6,8,1,0,0,1,1,3,2,2,2,6,8,4,7,8,6,7,5,1,5,5,0,4,1,1,5,6,8,2,4,8,7,1,7,4,5,6,2,6,2,5,0,6,1,7,7,2,6,5,4,6,7,4,1,6,5,1,5,6,2,6],
    -1: [1,6,8,1,6,2,2,8,5,0,6,4,3,2,8,7,0,0,1,3,7,1,4,5,3,8,6,4,1,0,6,0,4,0,6,5,6,0,6,4,1,0,5,6,6,3,0,4,1,3,5,5,0,7,8,8,4,6,4,3,4,6,8,5,5,0,6,7]
}

test_board = Board()
test_board.pieces[:][:] = 0
test_board.pieces[0][:64] = 1
test_board.pieces[0][80:] = -1
test_board.pieces[1][0] = 1
test_board.pieces[2][0] = 1
test_board.pieces[4][0] = -1
test_board.pieces[5][0] = 1
test_board.pieces[6][0] = 1
test_board.pieces[7][0] = 1
test_board.pieces[8][:5] = 1
test_board.pieces[9][:2] = 1

test_board.pieces[2][161] = -1
test_board.pieces[3][161] = 1
test_board.pieces[7][161] = -1
test_board.pieces[8][161] = -1
test_board.pieces[9][161] = -1
# MOVE #136
# -1 makes action #8
# env_loc.tuzdyq[0]: 11
# env_loc.tuzdyq[1]: 3
# ============================================================================================================================================================================
# 064|0|XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX----------------OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO|0|082
# 001|1|X-----------------------------------------------------------------------------------------------------------------------------------------------------------------|1|000
# 001|2|X----------------------------------------------------------------------------------------------------------------------------------------------------------------O|2|001
# 000|3|-----------------------------------------------------------------------------------------------------------------------------------------------------------------X|3|000
# 000|4|O-----------------------------------------------------------------------------------------------------------------------------------------------------------------|4|000
# 001|5|X-----------------------------------------------------------------------------------------------------------------------------------------------------------------|5|000
# 001|6|X-----------------------------------------------------------------------------------------------------------------------------------------------------------------|6|000
# 001|7|X----------------------------------------------------------------------------------------------------------------------------------------------------------------O|7|001
# 005|8|XXXXX------------------------------------------------------------------------------------------------------------------------------------------------------------O|8|001
# 002|9|XX---------------------------------------------------------------------------------------------------------------------------------------------------------------O|9|001
# ============================================================================================================================================================================
# Full board stones: 162
# -1 won game

class TestListElements(unittest.TestCase):
    def setUp(self):
        self.expected = test_board.pieces
        game = TogyzQumalaqGame(10, 162)
        board = Board()
        moves = {1: [], -1: []}
        player = 1
        #print(f'MOVE #0')
        game.display_board(board.pieces)
        j = 0
        for i in range(136):
            move = MOVES[player][j]
            if i % 2 != 0:
                j += 1
            moves[player].append(move)
            #print(f'MOVE #{i + 1}')
            #print(f'{player} makes action #{move + 1}')
            pieces, player = game.getNextState(board.pieces, player, move)
            board.pieces = pieces
            game.display_board(board.pieces)
            if game.getGameEnded(board.pieces, player) != 0:
                #print(f'{game.getGameEnded(board.pieces, player)} won game')
                break
        self.result = board.pieces

    def test_play_game(self):
        """Will succeed"""
        self.assertEqual(self.result.tolist(), self.expected.tolist())


if __name__ == "__main__":
    unittest.main()