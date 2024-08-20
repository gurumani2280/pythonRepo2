class Shape:
    def calculateArea(self):
        print("To calculate area create object of a defined shape of Circle,square,triangle ....")#This print statement will over written by child class

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
    def calculateArea(self):
        print("Area of Square is ", self.length ** 2)

obj1 = Square(5)
obj1.calculateArea()
objShape=Shape()
objShape.calculateArea()#To calculate area create object of a defined shape of Circle,square,triangle ....
"""
o/p:
Constructor of Square 5
Constructure of Rectangle  5 5
Area of Square is  25
"""