
class A:
    def feature1(self):
        print("Feature1 of Class A")
class B:
    def feature1(self):
        print("Feature1 of Class B")
class C(B,A):
    def feature1(self):
        print("Feature1 of Class C")
obj1=C()
obj1.feature1()
"""
Feature1 of Class C#what ever given in the child class, that get over written, so child class will execute in priority
"""

