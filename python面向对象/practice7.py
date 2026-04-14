class Animal:
    def __init__(self,name):
        self.name=name
class bird(Animal):
    def __init__(self, name,wingspan):
        self.wingspan=wingspan
        super().__init__(name)
    def __str__(self):
        print(f"{self.name},{self.wingspan}")