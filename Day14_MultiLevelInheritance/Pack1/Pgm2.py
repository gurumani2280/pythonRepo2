#Multilevel inheritance
class A:#parent class of B/grand parent of C
    def __init__(self,name,roleNum):
        print("init method/Constructor of Class A")
        self.name=name
        self.roleNum=roleNum
class B(A):#Child of A or/and parent class of C
    def __init__(self,name,roleNum,age):
        print("init method/Constructor of Class B")
        super().__init__(name,roleNum)
        self.age=age
class C(B):#Child of B or/and grand child of A
    def __init__(self,name,roleNum,age,city):
        print("init method/Constructor of Class C")
        super().__init__(name,roleNum,age)
        self.city=city
obj1=C("Aby",111,30,"tvm")
"""
O/p:
init method/Constructor of Class C
init method/Constructor of Class B
init method/Constructor of Class A
"""



