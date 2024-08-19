#Inheritance
class Person:
    def __init__(self,firstName,lastname):
        print("Arg constructor of person class : ",firstName,lastname)
        self.firstname=firstName#instance variable
        self.lastname=lastname

    def printName(self):
        print(self.firstname,self.lastname)

class Student(Person):
    def __init__(self,firstname,lastname):
        print("No arg constructor of student class")
        super().__init__(firstname,lastname)
objstudent=Student("soni","kk")
objstudent.printName()



