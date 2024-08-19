#Inheritance
class Person:
    def __init__(self,firstName,lastname):
        print("Arg constructor of person class : ",firstName,lastname)
        self.firstname=firstName
        self.lastname=lastname

    def printName(self):
        print(self.firstname,self.lastname)
#obj1=Person("Python","programming")#Arg constructor of person class :  Python programming
#obj1.printName()#Python programming

class Student(Person):
    pass
objStudent=Student("Sony","kk")#Arg constructor of person class :  Sony kk
objStudent.printName()#Sony kk
