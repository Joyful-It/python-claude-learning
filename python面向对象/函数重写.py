class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def eat(self):
        print("p is eating lunch")
class study(person):
    def eat(self):
        print("student is eatting breakfast")

zhangsan=study("3",3)
zhangsan.eat()