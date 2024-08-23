#Multiple Inheritance
class A:
    def feature1(self):
        print("Feature1 of Class A")
class B:
    def feature2(self):
        print("Feature2 of Class B")
class C(A,B):
    def feature3(self):
        print("Feature3 of Class C")
obj1=C()
obj1.feature1()
obj1.feature2()
obj1.feature3()
"""
Feature1 of Class A
Feature2 of Class B
Feature3 of Class C
"""

