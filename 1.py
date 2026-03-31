MOD = 998244353
n,a0=map(int,input().spilt())
add=0
mul=[]
for _ in range(n):
    op,num=input().spilt()
    num=int(num)
    if op == '+':
        add+=num
    else:
        mul.append(num)
a0=(a0+add)%MOD
for num in mul:
    a0=(a0*num)%MOD
print(a0)
