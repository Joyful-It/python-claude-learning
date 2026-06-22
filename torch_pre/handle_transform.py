import torch
X = torch.randn(4,512)
W_Q = torch.randn(512, 64)   # Q 的投影矩阵
W_K = torch.randn(512, 64)   # K 的投影矩阵
W_V = torch.randn(512, 64)   # V 的投影矩阵


Q=X@W_Q
K=X@W_K
V=X@W_V

print(Q.shape)
print(X)