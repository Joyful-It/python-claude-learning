class Book:
    def __init__(self,name,author,price):
        self.name=name
        self.author=author
        self.price=price
    def read(self):
        print(f"reading <<{self.name}>>")
xiyouji=Book("xiyou","wu",30)
xiyouji.price=50
xiyouji.read()
print(xiyouji.price)