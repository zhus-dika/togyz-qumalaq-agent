import numpy as np
from TogyzQumalaq.TogyzQumalaqEnv import TogyzQumalaqEnv
class AverageMeter(object):
    """From https://github.com/pytorch/examples/blob/master/imagenet/main.py"""

    def __init__(self):
        self.val = 0
        self.avg = 0
        self.sum = 0
        self.count = 0

    def __repr__(self):
        return f'{self.avg:.2e}'

    def update(self, val, n=1):
        self.val = val
        self.sum += val * n
        self.count += n
        self.avg = self.sum / self.count


class dotdict(dict):
    def __getattr__(self, name):
        return self[name]

def convertTogyzQumalaq2Board(env):
    '''
    :param env: TogyzQumalaq PettingZoo environment
    :return: board - numpy array [2, 162, 162] sizes
    '''
    total_qumalaqs = 0
    n_x = 10
    n_y = 162
    pieces = np.zeros((n_x, n_y))
    # ===================
    # fill pieces by otaular info
    for i, otau in enumerate(env.otaular):
        for j in range(otau):
            if i < 9:
                if i != env.tuzdyq[1]:
                    pieces[i + 1][j] = 1
                    total_qumalaqs += 1
            else:
                if i != env.tuzdyq[0] - 9:
                    pieces[i - 8][n_y - 1 - j] = -1
                    total_qumalaqs += 1
    # ===================
    # fill pieces by tuzdyq info

    if env.tuzdyq[0] >= 0:
        pieces[env.tuzdyq[0] - 8][n_y - 1] = 1
    if env.tuzdyq[1] >= 0:
        pieces[env.tuzdyq[1] + 1][0] = -1

    # ===================
    # fill pieces by qazandar info
    stones = env.qazandar[0]
    total_qumalaqs += stones

    for j in range(stones):
            pieces[0][j] = 1
    stones = env.qazandar[1]
    total_qumalaqs += stones

    for j in range(stones):
        pieces[0][n_y - 1 - j] = -1

    assert total_qumalaqs == 162, f"Error from convertTogyzQumalaq2Board: Total qumalaqs is not equal to 162: {total_qumalaqs} observation: otaular - {env.otaular}, qazandar - {env.qazandar}, tuzdyq - {env.tuzdyq}"
    return pieces
    
def convertBoard2TogyzQumalaq(board_pieces, player):
    total_qumalaqs = 0
    env = TogyzQumalaqEnv()
    env.reset()
    if player == -1:
        env.agent_selection = env._agent_selector.next()
    # ==================
    # fill qazandar
    n_x = board_pieces.shape[0]
    n_y = board_pieces.shape[1]

    for j in range(n_y - 1):
        if board_pieces[0][j] > 0:
            env.qazandar[0] += 1
            total_qumalaqs += 1
        if board_pieces[0][n_y - 1 - j] < 0:
            env.qazandar[1] += 1
            total_qumalaqs += 1
    # ==================
    # fill tuzdyq
    for i in range(1, n_x):
        if board_pieces[i][0] < 0:
            env.tuzdyq[1] = i - 1

        if board_pieces[i][n_y - 1] > 0:
            env.tuzdyq[0] = i + 8

    for i in range(1, n_x):
        cnt = 0
        while board_pieces[i][cnt] > 0:
            cnt += 1

        env.otaular[i - 1] = cnt
        total_qumalaqs += cnt
        cnt = 0
        while board_pieces[i][n_y - 1 - cnt] < 0:
                cnt += 1
        env.otaular[i + 8] = cnt
        total_qumalaqs += cnt
    assert total_qumalaqs == 162, f"Error from convertBoard2TogyzQumalaq: Total qumalaqs is not equal to 162: {total_qumalaqs} observation: otaular - {env.otaular}, qazandar - {env.qazandar}, tuzdyq - {env.tuzdyq}"
    return env