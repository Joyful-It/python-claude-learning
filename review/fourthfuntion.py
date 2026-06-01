def demo(a,b=10,*num,**key):
    print("a=",a)
    print(f'b={b}')
    print(f'num={num}')
    print(f'key={key}')


a=demo(23,34,2,3,x=90,y=13)

def order_food(table_number,discount=1.0,*food_number,**tips):
    print(f"table_number{table_number}")
    print(f"discount{discount}")
    print(f'food_number{food_number}')
    print(f"tips{tips}")

bowen=order_food(5,0.85,'宫保鸡丁','shuizhuyu',less_oil=True)
print(bowen)