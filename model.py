import torch
import numpy as np
import torch.nn as nn
from torch.nn import Conv1d,ReLU,MaxPool1d,Linear

class CNN_Net(nn.Module):
    def __init__(self):
        super().__init__()
        
        self.features = nn.Sequential(
            Conv1d(3, 64, kernel_size=3, stride=1, padding=1)
            # 300, 64, 5000
            ,ReLU(inplace=True)
            ,MaxPool1d(kernel_size=2, stride=2, padding=0, dilation=1, ceil_mode=False)
            # 300, 64, 2500
            ,Conv1d(64, 128, kernel_size=3, stride=1, padding=1)
            ,ReLU(inplace=True)
            # 300, 128, 2500
            ,MaxPool1d(kernel_size=2, stride=2, padding=0, dilation=1, ceil_mode=False)
            # 300, 128, 1250
            ,Conv1d(128, 256, kernel_size=3, stride=1, padding=1)
            ,ReLU(inplace=True)
            # 300, 256, 1250
            ,Conv1d(256, 256, kernel_size=3, stride=1, padding=1)
            ,ReLU(inplace=True)
            # 300, 256, 1250
            ,MaxPool1d(kernel_size=2, stride=2, padding=0, dilation=1, ceil_mode=False)
            # 300, 256, 625
            ,Conv1d(256, 512, kernel_size=3, stride=1, padding=1)
            ,ReLU(inplace=True)
            # 300, 512, 625
            ,Conv1d(512, 512, kernel_size=3, stride=1, padding=1)
            ,ReLU(inplace=True)
            # 300, 512, 625
            ,MaxPool1d(kernel_size=2, stride=2, padding=0, dilation=1, ceil_mode=False)
            # 300, 512, 312
            ,Conv1d(512, 512, kernel_size=3, stride=1, padding=1)
            ,ReLU(inplace=True)
            # 300, 512, 312
            ,Conv1d(512, 512, kernel_size=3, stride=1, padding=1)
            ,ReLU(inplace=True)
            # 300, 512, 312
            ,MaxPool1d(kernel_size=2, stride=2, padding=0, dilation=1, ceil_mode=False)
            # 300, 512, 156
        )
        
        self.classifier = nn.Sequential(
            Linear(512*156,100)
        )
    def forward(self,x):
        
        out = self.features(x)
        out = torch.flatten(out,1)
        out = self.classifier(out)
  
        return out   

