class Phone:
    def __init__(self,brand,type,price):
        self.brand=brand
        self.type=type
        self.price=price
    def call(self):
        print(f"{self.brand}{self.type} is calling")

huawei=Phone("huawei","meta8","7000")
huawei.call()
oppo=Phone("oppp","findx9","7000")
oppo.call()