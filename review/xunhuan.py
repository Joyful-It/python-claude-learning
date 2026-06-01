for i in range(1,6):
    print(i*i)

scores = [85, 92, 78, 60, 55]
for i in scores:
    if i >60:
        print(f'大于60的值:{i}')


a=0
b=1
while(b<=100):
    a=a+b
    b+=1
print(a)


def calculate(a, b):
    print(a + b)
    # return a + b

result = calculate(4, 6)
# print("结果是：", result)


answer=7

while True:
    a=int(input())
    if a>answer:
        print('da')
    elif a<answer:
        print('xiao')
    else:
        print('dui')
        break



