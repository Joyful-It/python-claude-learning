class Employee:
    def __init__(self,salary):
        self.__salary=salary
    def set_salary(self,new_salay):
        if new_salay>0:
           self.__salary=new_salay
           print("ok")
        else:
            print("salary is low")
    def get_salary(self):
        return self.__salary
    def work(self):
        print("work")
wang=Employee(1000)
wang.set_salary(40)
print(wang.get_salary())