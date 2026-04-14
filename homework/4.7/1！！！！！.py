"""
程序功能=计算圆的周长和面积
"""
PI=3.14
R=float(input("输入半径："))
L=round(PI*R,2)
S=round(PI*R*R,2)
print("da" if S>100 else "xiao")
print("banjing",R)
print("zhouchang",L)
print(f"zhi:{S},leixing{type(S)}")

#保留一位小数三种方式
print(f"bao liu yi wei :{PI:.1f}")#保留一位小数
print("{:.1f}",format(PI))

#end 用法

