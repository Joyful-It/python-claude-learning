class Student:
    def __init__(self,name:str,age:int):
        self.name=name
        self.age=age

    def say_hello(self):
        print("hello")
lihhua=Student("lihua",12)
print(lihhua.age)
print(lihhua.say_hello())
lihhua.say_hello()