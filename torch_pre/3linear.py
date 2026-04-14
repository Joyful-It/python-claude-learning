import torch
import torch.nn as nn

layer= nn.Linear(in_features=3,out_features=5)
layer1=nn.Linear(4,2)

print(layer.weight)
print(layer.bias)
print(layer1.weight)