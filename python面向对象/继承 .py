class animal:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def eat(self):
        print(f"{self.name} is eating")
class dog(animal):
    def bark(self):
        print(f"{self.name} is barking")

class cat(animal):
    def eat(self):
        print(f"{self.name} is eating")

dahuang=dog("dahuang",3)
mimi=cat("mimi",5)

print(dahuang.name)
