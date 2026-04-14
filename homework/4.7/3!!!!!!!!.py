# 大作业 3
# 1. 多行注释：成绩评级系统
# 2. 输入考试成绩（0~100，float）
# 3. 使用 if-elif-else 判断等级：
# 90~100：优秀
# 80~89：良好
# 60~79：及格
# 0~59：不及格
# 4. 用逻辑运算符判断：成绩是否合法（0≤成绩≤100）
# 5. 输出成绩、等级、是否合法
'''
成绩评级系统'''
try:
    score=float(input("请输入考试成绩0-100，浮点数："))
    is_vail=0<=score<=100

    if is_vail:
        if 90<=score<=100:
            print("prefect")
        elif 80<=score<=89:
            print("good")
        elif 60<=score<=79:
            print("ok")
        else:
            print("not ok")
        print(f"grade{score}")
    else:
        print("buhege")
    
except ValueError:
    print("qingshuru float")


    
