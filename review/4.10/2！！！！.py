# 计算圆柱体积并判断
PI=3.1415926
HEIGHT =10
R=float(input("ban jing :"))
V=round(PI*R*R*HEIGHT,2)+50# 直接保留两位小数
if not( V<1000 or V>3000):#   取反
    print ("zai")
else:
    print("not")
    

