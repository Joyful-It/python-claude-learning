class Computer :
    def __init__(self,brand,price):
        self.brand=brand
        self.price=price
    def work(self):
        print(f"{self.brand}is running big model")
huashuo=Computer("huashuo",1000)
huashuo.work()