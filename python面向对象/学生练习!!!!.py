class student:
    def __init__(self,name,age,ic):
        self.name=name
        self.age=age
        self.ic=ic
    def study(self):
        print(f"{self.name} is studying python model ")
class colleague(student):
    def __init__(self, name, age,ic,major):
        self.major=major
        super().__init__(name,age,ic)
    def study(self):
        print(f"{self.major} is studying big model")
class graduatesStudent(student):#注意类要对齐，return是返回，不是打印
    def __init__(self, name, age, ic):
        super().__init__(name, age, ic)
    def study(self):
        print(f"{self.ic} is import")
def do_study(obj):# 多态函数写在外面！
        obj.study()# student 是类名，不是对象！多态要传递对象
        

lisan=student("lisan",18,123)
print(lisan.name)
lisan.study()
zhangsi=colleague("zhangsi",19,345,"AI")
zhangsi.study()
# 多态：同一个函数，不同的对象，不同的结果
do_study(lisan)
do_study(zhangsi)