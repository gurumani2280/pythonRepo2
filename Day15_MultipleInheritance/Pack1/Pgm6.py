
class A:
    def feature1(self):
        print("Feature1 of Class A")
class B:
    def feature1(self):
        print("Feature1 of Class B")
class C(A,B):
    def feature1(self):
        print("Feature1 of Class C")
        super().feature1()
obj1=C()
obj1.feature1()
"""
Feature1 of Class C
Feature1 of Class A
"""

