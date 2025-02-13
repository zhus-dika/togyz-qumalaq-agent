import sys
sys.path.append('../..')
from utils import *

import argparse
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim

# class TogyzQumalaqNNet(nn.Module):
#     def __init__(self, game, args):
#         # game params
#         self.board_x, self.board_y = game.getBoardSize()
#         self.action_size = game.getActionSize()
#         self.args = args
#
#         super(TogyzQumalaqNNet, self).__init__()
#
#         # Convolutional nets
#         self.conv1 = nn.Conv2d(1, args.num_channels, 3, stride=1, padding=1)
#         self.conv2 = nn.Conv2d(args.num_channels, args.num_channels, 3, stride=1, padding=1)
#         self.conv3 = nn.Conv2d(args.num_channels, args.num_channels, 3, stride=1, padding=1)
#         self.conv4 = nn.Conv2d(args.num_channels, args.num_channels, 3, stride=1, padding=1)
#         # self.conv5 = nn.Conv2d(args.num_channels, args.num_channels, 3, stride=1, padding=1)
#         # self.conv6 = nn.Conv2d(args.num_channels, args.num_channels, 3, stride=1, padding=1)
#
#         self.bn1 = nn.BatchNorm2d(args.num_channels)
#         self.bn2 = nn.BatchNorm2d(args.num_channels)
#         self.bn3 = nn.BatchNorm2d(args.num_channels)
#         self.bn4 = nn.BatchNorm2d(args.num_channels)
#         # self.bn5 = nn.BatchNorm2d(args.num_channels)
#         # self.bn6 = nn.BatchNorm2d(args.num_channels)
#
#         # Pooling
#         self.pool = nn.MaxPool2d(2, 2)  # Reduce
#
#         # Полносвязные слои
#         self.fc1 = nn.Linear(args.num_channels * self.board_x // 2 * self.board_y // 2, 2048)
#         self.fc_bn1 = nn.BatchNorm1d(2048)
#
#         self.fc2 = nn.Linear(2048, 512)
#         self.fc_bn2 = nn.BatchNorm1d(512)
#
#         self.fc3 = nn.Linear(512, self.action_size)
#         self.fc4 = nn.Linear(512, 1)
#
#     def forward(self, s):
#         s = s.view(-1, 1, self.board_x, self.board_y)
#
#         # Свертки + пулинг
#         s = F.relu(self.bn1(self.conv1(s)))
#         s = F.relu(self.bn2(self.conv2(s)))
#         s = F.relu(self.bn3(self.conv3(s)))
#         s = F.relu(self.bn4(self.conv4(s)))
#         # s = F.relu(self.bn5(self.conv5(s)))
#         # s = F.relu(self.bn6(self.conv6(s)))
#
#         # Pooling
#         s = self.pool(s)
#
#         s = s.view(-1, self.args.num_channels * self.board_x // 2 * self.board_y // 2)
#
#         # Fully connected layers
#         s = F.dropout(F.relu(self.fc_bn1(self.fc1(s))), p=self.args.dropout, training=self.training)
#         s = F.dropout(F.relu(self.fc_bn2(self.fc2(s))), p=self.args.dropout, training=self.training)
#
#         # Outputs
#         pi = self.fc3(s)  # Policy
#         v = self.fc4(s)   # Estimation of the position
#
#         return F.log_softmax(pi, dim=1), torch.tanh(v)

class ResidualBlock(nn.Module):
    def __init__(self, channels):
        super(ResidualBlock, self).__init__()
        self.conv1 = nn.Conv2d(channels, channels, kernel_size=3, stride=1, padding=1, bias=False)
        self.bn1 = nn.BatchNorm2d(channels)
        self.conv2 = nn.Conv2d(channels, channels, kernel_size=3, stride=1, padding=1, bias=False)
        self.bn2 = nn.BatchNorm2d(channels)

    def forward(self, x):
        residual = x  # Skip connection
        out = F.relu(self.bn1(self.conv1(x)))
        out = self.bn2(self.conv2(out))
        out += residual  # Add input (skip connection)
        return F.relu(out)

class TogyzQumalaqNNet(nn.Module):
    def __init__(self, game, args):
        super(TogyzQumalaqNNet, self).__init__()

        self.board_x, self.board_y = game.getBoardSize()
        self.action_size = game.getActionSize()
        self.args = args
        num_channels = args.num_channels

        # Initial convolutional layer
        self.conv1 = nn.Conv2d(1, num_channels, kernel_size=3, stride=1, padding=1, bias=False)
        self.bn1 = nn.BatchNorm2d(num_channels)

        # Residual-blocks
        self.res1 = ResidualBlock(num_channels)
        self.res2 = ResidualBlock(num_channels)
        self.res3 = ResidualBlock(num_channels)
        self.res4 = ResidualBlock(num_channels)

        # Pooling
        self.pool = nn.MaxPool2d(2, 2)  # Reduce dimension

        # FC layers
        reduced_x, reduced_y = self.board_x // 2, self.board_y // 2  # After pooling
        self.fc1 = nn.Linear(num_channels * reduced_x * reduced_y, 1024)
        self.fc_bn1 = nn.BatchNorm1d(1024)

        self.fc2 = nn.Linear(1024, 512)
        self.fc_bn2 = nn.BatchNorm1d(512)

        self.fc3 = nn.Linear(512, self.action_size)  # Policy
        self.fc4 = nn.Linear(512, 1)  # Position's estimation

    def forward(self, s):
        s = s.view(-1, 1, self.board_x, self.board_y)

        # Initial convolutional layer
        s = F.relu(self.bn1(self.conv1(s)))

        # Residual-блоки
        s = self.res1(s)
        s = self.res2(s)
        s = self.res3(s)
        s = self.res4(s)

        # Pooling
        s = self.pool(s)

        # Transformation for fully connected layers
        s = s.view(-1, self.args.num_channels * (self.board_x // 2) * (self.board_y // 2))

        # Fully connected layers
        s = F.dropout(F.relu(self.fc_bn1(self.fc1(s))), p=self.args.dropout, training=self.training)
        s = F.dropout(F.relu(self.fc_bn2(self.fc2(s))), p=self.args.dropout, training=self.training)

        # Outputs
        pi = self.fc3(s)  # Policy head
        v = self.fc4(s)   # Value head

        return F.log_softmax(pi, dim=1), torch.tanh(v)