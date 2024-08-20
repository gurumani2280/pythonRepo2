#Multilevel inheritance
class A:#parent class of B/grand parent of C
    def feature1(self):
        print("Feature1 of Class A ")
class B(A):#Child of A or/and parent class of C
    def feature2(self):
        print("Feature2 of Class B ")
class C(B):#Child of B or/and grand child of A
    def feature3(self):
        print("Feature3 of Class C ")
obj1=C()
obj1.feature1()#Feature1 of Class A
obj1.feature2()#Feature2 of Class B
obj1.feature3()#Feature3 of Class C



