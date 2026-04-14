class Vehicle:
    def __init__(self,brand,speed,):
        self.brand=brand
        self.speed=speed
    def run(self):
        print("123")

class bicycle(Vehicle):
    def __init__(self, brand, speed,material):
        self.material=material
        super().__init__(brand, speed)
    def run(self):
        print("234")

    def __str__(self):
        return f"{self.brand}"
a=bicycle("a",12,"glass")
a.run()

print(a.__str__())
# #def _str_(self)
#  return f"{self.brand}"
# # a=bicycle("a",12,"glass")
# a.run()
#a._str_()  这是我自己创建的函数比正常str少两个下划线，需要自己调用
#如果是双下划线str 就是不用调用
# print(a.__str__())


