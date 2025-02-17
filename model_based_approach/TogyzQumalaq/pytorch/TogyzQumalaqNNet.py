import sys
sys.path.append('../..')
from utils import *

import torch
import torch.nn as nn
import torch.nn.functional as F

class ResidualBlock(nn.Module):
    def __init__(self, channels):
        super(ResidualBlock, self).__init__()
        self.conv1 = nn.Conv2d(channels, channels, kernel_size=3, stride=1, padding=1)
        self.bn1 = nn.BatchNorm2d(channels)
        self.conv2 = nn.Conv2d(channels, channels, kernel_size=3, stride=1, padding=1)
        self.bn2 = nn.BatchNorm2d(channels)

    def forward(self, x):
        residual = x
        out = F.relu(self.bn1(self.conv1(x)))
        out = self.bn2(self.conv2(out))
        out += residual  # Skip connection
        return F.relu(out)

class TogyzQumalaqNNet(nn.Module):
    def __init__(self, game, args):
        super(TogyzQumalaqNNet, self).__init__()
        self.board_x, self.board_y = game.getBoardSize()
        self.action_size = game.getActionSize()
        self.args = args

        self.conv1 = nn.Conv2d(1, args.num_channels, kernel_size=3, stride=1, padding=1)
        self.bn1 = nn.BatchNorm2d(args.num_channels)

        self.residual_blocks = nn.Sequential(
            *[ResidualBlock(args.num_channels) for _ in range(args.residual_blocks)]
        )

        # Policy head
        self.policy_conv = nn.Conv2d(args.num_channels, 128, kernel_size=1)
        self.policy_bn = nn.BatchNorm2d(128)
        self.policy_fc = nn.Linear(128 * self.board_x * self.board_y, self.action_size)

        # Value head
        self.value_conv = nn.Conv2d(args.num_channels, 64, kernel_size=1)
        self.value_bn = nn.BatchNorm2d(64)
        self.value_fc1 = nn.Linear(64 * self.board_x * self.board_y, 256)
        self.value_fc2 = nn.Linear(256, 1)

    def forward(self, s):
        s = s.view(-1, 1, self.board_x, self.board_y)  # (batch_size, 1, board_x, board_y)
        s = F.relu(self.bn1(self.conv1(s)))
        s = self.residual_blocks(s)

        # Policy head
        p = F.relu(self.policy_bn(self.policy_conv(s)))
        p = p.view(p.size(0), -1)
        p = self.policy_fc(p)

        # Value head
        v = F.relu(self.value_bn(self.value_conv(s)))
        v = v.view(v.size(0), -1)
        v = F.relu(self.value_fc1(v))
        v = self.value_fc2(v)

        return F.log_softmax(p, dim=1), torch.tanh(v)