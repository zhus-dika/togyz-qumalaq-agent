import sys


NUM_ITERS = 1000
PLAYS = {"bastaushy": 0, "qostaushy": 0}
REWARDS = {"bastaushy": [], "qostaushy": []}
sys.path.append('./')
from model_based_approach.utils import *

from model_based_approach.TogyzQumalaq.TogyzQumalaqLogic import Board
from model_based_approach.TogyzQumalaq.TogyzQumalaqGame import TogyzQumalaqGame

for _ in range(200):
    game = TogyzQumalaqGame(10, 34)
    board = Board()

    player = 1
    moves = {1: [], -1: []}
    print(f'MOVE #0')
    game.display_board(board.pieces)
    for i in range(350):
        val_moves = game.getValidMoves(board.pieces, player)

        move = np.random.choice(np.nonzero(val_moves)[0], 1)[0]
        moves[player].append(move)
        print(f'MOVE #{i + 1}')
        print(f'{player} makes action #{move + 1}')
        pieces, player = game.getNextState(board.pieces, player, move)
        board.pieces = pieces
        env_loc = convertBoard2TogyzQumalaq(pieces, player)
        game.display_board(board.pieces)

        if game.getGameEnded(board.pieces, player) != 0:
            print(f'{game.getGameEnded(board.pieces, player)} won game')
            break