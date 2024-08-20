class Shape:
    def calculateArea(self):
        print("To calculate area create object of a defined shape of Circle,square,triangle ....")

class Rectangle(Shape):
    def __init__(self,length,width):
        print("Constructure of Rectangle ",length,width)
        self.length=length
        self.width=width
    def calculateArea(self):
        print("Area of Rectangle is ",self.length*self.width)
class Square(Rectangle):
    def __init__(self,side):
        print("Constructor of Square",side)
        super().__init__(side,side)
obj1=Square(5)
obj1.calculateArea()
"""
O/p:
Constructor of Square 5
Constructure of Rectangle  5 5
Area of Rectangle is  25
"""

