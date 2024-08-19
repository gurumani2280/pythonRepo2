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
    def __init__(self):
        print("No arg constructor of student class")
#objStudent=Student("Sony","kk")
#objStudent.printName()#Sony kk""" #IndentationError: expected an indented block after function definition on line 14
objStudent2=Student()#No arg constructor of student class
objStudent2.printName()#AttributeError: 'Student' object has no attribute 'firstname'

