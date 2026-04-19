class car :
    def __init__(self,brand:str,color:str,price:float,year:int=2014):
        self.brand=brand
        self.color=color
        self.price=price
        self.year=year
    def show_info(self):
        print(f"show all :{self.price},{self.brand},{self.color},{self.year}")
    def get_discount(self):
        discount=float(input("please enter discount:"))
        print(f"after price:{self.price*discount}")
bba=car("bba","red",123.4)
bba.show_info()
bba.get_discount()