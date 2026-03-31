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


