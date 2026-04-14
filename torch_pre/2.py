import torch
x=torch.tensor([2.0,3.0],requires_grad=True)#创建一个需要梯度的tensor 
                                            #requires 是对tesnor的运算的追踪

y=x**2+2*x+1# 定义运算
y.sum().backward()# 反向传播 求导！！！！！！！！！！！！
print("x",x)
print("y",y)
print("x.grade:",x.grad)#x。grade 是对式子求导的结果
