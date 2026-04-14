#判断输入数字的奇偶性与大小范围
num=int(input("接受用户输入的整数："))
if num %2 ==0 and num>50:
    print("ok")
else:
    print("not")
if num>100:
    print("super")
elif 50<num<100:
    print("big")
else:
    print("usually")