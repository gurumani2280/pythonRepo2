
class A:
    def feature1(self):
        print("Feature1 of Class A")
class B:
    def feature1(self):
        print("Feature1 of Class B")
class C(A,B):
    def feature3(self):
        print("Feature3 of Class C")
obj1=C()
obj1.feature1()# It will call class A, since class A is given first while inheriting
obj1.feature3()
"""
Feature1 of Class A
Feature3 of Class C
"""

