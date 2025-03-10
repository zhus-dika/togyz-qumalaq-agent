import Arena
from MCTS import MCTS
from TogyzQumalaq.TogyzQumalaqGame import TogyzQumalaqGame
from TogyzQumalaq.TogyzQumalaqPlayers import *
from TogyzQumalaq.pytorch.NNet import NNetWrapper as NNet


import numpy as np
from utils import *

"""
use this script to play any two agents against each other, or play manually with
any agent.
"""

g = TogyzQumalaqGame(10, 32)

# all players
rp = RandomPlayer(g).play
hp = HumanTogyzQumalaqPlayer(game=g, n_x=10, n_y=32).play



# nnet players
n1 = NNet(g)
n1.load_checkpoint('./trained_models/mcts','temp.pth.tar')
# n1.load_checkpoint('./temp','checkpoint_5.pth.tar')
args1 = dotdict({'numMCTSSims': 50, 'cpuct':1.0}) # numMCTSSims - Number of games moves for MCTS to simulate
mcts1 = MCTS(g, n1, args1)
n1p = lambda x: np.argmax(mcts1.getActionProb(x, temp=0))

arena = Arena.Arena( n1p, rp, g)#, display=TogyzQumalaqGame.display_board)
# arena = Arena.Arena(rp, rp, g, display=TogyzQumalaqGame.display_board)
# print(arena.playGames(20, verbose=True))
print(arena.playGames(20))