class student:
    def __init__(self,name,age,ic):
        self.name=name
        self.__age=age
        self._ic=ic

    def study():
        print(f"{self.name} is studying python model ")
lisan=student("lisan",18,123)
lisan.__age=100
print(lisan.__age)
print(lisan._student__age)