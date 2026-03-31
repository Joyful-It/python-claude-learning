class Bank:
    def __init__(self, money):
        self.__money = money
    
    # 请你写 get_money 方法
    def get_money(self):
        return self.__money
    # 请你写 set_money 方法（验证：金额不能为负）
    def set_money(self,new_self):
        if new_self>0:
            self.__money=new_self
            print("ok")
        else:
            print("not")
bank = Bank(1000)
print(bank.get_money())    # 应该输出 1000
bank.set_money(500)        # 应该成功
bank.set_money(-100)       # 应该提示错误
