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

g = TogyzQumalaqGame(10, 162)

# all players
rp = RandomPlayer(g).play
hp = HumanTogyzQumalaqPlayer(game=g, n_x=10, n_y=162).play



# nnet players
n1 = NNet(g)
n1.load_checkpoint('./models/mcts/','best.pth.tar')
args1 = dotdict({'numMCTSSims': 50, 'cpuct':1.0})
mcts1 = MCTS(g, n1, args1)
n1p = lambda x: np.argmax(mcts1.getActionProb(x, temp=0))

player2 = hp

arena = Arena.Arena(n1p, player2, g, display=TogyzQumalaqGame.display_board)

print(arena.playGames(2, verbose=True))