# 1. 多行注释：个人所得税简易计算
# 2. 常量： TAX_RATE = 0.1
# 3. 输入税前收入（float）
# 4. 计算税后收入 = 税前 × (1-TAX_RATE)，保留 2 位小数
# 5. 三目运算：税后≥5000 → “高收入”，否则 “普通收入”
# 6. if 判断：税后收入是否为偶数
# 7. 输出：税前、税后、收入等级、是否为偶数、所有类型

'''个人所得税简易计算'''
TAX_RATE = 0.1
pre_TAX=float(input("输入税前："))
back_TAX=round(pre_TAX*(1-TAX_RATE),2)
print("high" if back_TAX>=5000 else "low")
if back_TAX %2 == 0:
    print("ok")
else:
    print("not ok")
print("qian:",pre_TAX)
print(f"hou {back_TAX},{type(back_TAX)}")

