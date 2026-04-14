import torch
import torch.nn as nn

layer= nn.Linear(3,5)

x=torch.tensor([1.0,2.0,3.0])

y=layer(x)
print("input:",x)
print("output:",y)
print("shape:",x.shape)
print("shape_y:",y)