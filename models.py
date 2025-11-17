"""Shared model definitions for MNIST digit classification."""

import torch
import torch.nn as nn
import torch.nn.functional as F


class SimpleCNN(nn.Module):
    """
    Simple CNN model for MNIST digit classification.
    
    Architecture:
    - Conv2d(1, 32, 3) -> ReLU
    - Conv2d(32, 64, 3) -> ReLU -> MaxPool2d(2)
    - Flatten -> Linear(9216, 128) -> ReLU
    - Linear(128, 10) -> Output
    """
    
    def __init__(self):
        super(SimpleCNN, self).__init__()
        self.conv1 = nn.Conv2d(1, 32, 3, 1)
        self.conv2 = nn.Conv2d(32, 64, 3, 1)
        self.fc1 = nn.Linear(9216, 128)
        self.fc2 = nn.Linear(128, 10)

    def forward(self, x):
        x = F.relu(self.conv1(x))
        x = F.relu(self.conv2(x))
        x = F.max_pool2d(x, 2)
        x = torch.flatten(x, 1)
        x = F.relu(self.fc1(x))
        x = self.fc2(x)
        return x
