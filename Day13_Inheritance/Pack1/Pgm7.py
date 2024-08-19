#Inheritance
class Person:
    def __init__(self,firstName,lastname):
        print("Arg constructor of person class : ",firstName,lastname)
        self.firstname=firstName#instance variable
        self.lastname=lastname

    def printName(self):
        print(self.firstname,self.lastname)

    def isStudent(self):
        print("Not a student")

class Student(Person):
    def __init__(self,firstname,lastname,graduationYear):
        print("No arg constructor of student class")
        super().__init__(firstname,lastname)
        self.graduationYear=graduationYear
    def isStudent(self):
        print("Is a student")

    def printgraduationYear(self):
        print("GraduationYear is ",self.graduationYear )

objstudent=Student("soni","kk",2014)
objstudent.printName()
objstudent.isStudent()#Is a student
objstudent.printgraduationYear()#GraduationYear is  2014




