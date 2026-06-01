class Restaurant:
    def __init__(self,name,cuisine,location,price,rating):
        self.name=name
        self.cuisine=cuisine
        self.location=location
        self.price=price
        self.rating=rating
    def __str__(self):
        return f"餐厅名字：{self.name},地址：{self.location},价格:{self.price}"
    