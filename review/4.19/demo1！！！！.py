class car : # ← 大写开头！！！！
    def __init__(self,brand:str,color:str,price:float,year:int=2014):
        self.brand=brand
        self.color=color
        self.price=price
        self.year=year
    def show_info(self):
        print(f"show all :{self.price},{self.brand},{self.color},{self.year}")
    def get_discount(self):
        discount=float(input("please enter discount:"))
        print(f"after price:{self.price*discount}")
bba=car("bba","red",123.4)
bba.show_info()
bba.get_discount()
# def __init__(self, brand: str, color: str, price: float, year: int = 2014):
# 这里的 float、str、int 只是告诉别人"应该传什么"，但 Python 不会真的检查。

 # ← 大写开头

#   def get_discount(self, discount_rate: float):
#         print(f"折后价格: {self.price * discount_rate}")
"""
类名 大写开头 class Car
    多个词用驼峰 class MyCar

    
变量 函数 小写 +下划线 my_car       discount=float(input("please enter discount:"))变量
   多个词描述 brand_name

常量  全大写 
"""