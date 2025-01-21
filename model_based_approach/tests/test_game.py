import gymnasium
import os, sys
import numpy as np
from gymnasium.spaces import Discrete, MultiDiscrete
from gymnasium import spaces

from IPython.display import clear_output
import time
from pettingzoo import AECEnv
from pettingzoo.utils import agent_selector, wrappers
import matplotlib.pyplot as plt
from tqdm.notebook import tqdm
import csv
import pandas as pd
#from scipy.interpolate import interp1d

import os
from typing import Optional, Tuple

from torch.utils.tensorboard import SummaryWriter
from tianshou.utils import TensorboardLogger

import gymnasium
import numpy as np
import torch
from copy import deepcopy
from tianshou.data import Collector, VectorReplayBuffer
from tianshou.env import DummyVectorEnv
from tianshou.env.pettingzoo_env import PettingZooEnv
from tianshou.policy import BasePolicy, DQNPolicy, RainbowPolicy, MultiAgentPolicyManager, RandomPolicy
from tianshou.trainer import OffpolicyTrainer
from tianshou.utils.net.common import Net

import random
import copy

NUM_ITERS = 1000
PLAYS = {"bastaushy": 0, "qostaushy": 0}
REWARDS = {"bastaushy": [], "qostaushy": []}

sys.path.append('../../model_based_approach')
from utils import *
sys.path.append('../../model_based_approach/TogyzQumalaq')
from TogyzQumalaqLogic import Board
from TogyzQumalaqGame import TogyzQumalaqGame

for _ in range(10):
    game = TogyzQumalaqGame(10, 162)
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