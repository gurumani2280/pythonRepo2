class Employee:
    companyName="UST"
    weeklyWorkingHours=45
    def __init__(self,name,id):
        print("constructor - it will get executed automatically whenever we create object for the class")
        self.name=name
        self.id=id

    def printEmployeeDetails(self):#self in argument for any method inside any class, which means it is a instance class
        print(f"Company Name: {self.companyName},Employee Name : {self.name},ID:{self.id}")

    @classmethod
    def displayWorkingHours(cls):
        print(f"Company Name : {cls.companyName},weekly Working Hour : {cls.weeklyWorkingHours}")

    @staticmethod
    def maximumOfTwoNum(a,b):
        return max(a,b)
Employee.displayWorkingHours()#Company Name : UST,weekly Working Hour : 45
obj1=Employee("Aby",10234)
obj1.printEmployeeDetails()#Company Name: UST,Employee Name : Aby,ID:10234
obj1.displayWorkingHours()#Company Name : UST,weekly Working Hour : 45
print(obj1.maximumOfTwoNum(5,10))#10
obj2=Employee("Manu",11123)
obj2.printEmployeeDetails()#Company Name: UST,Employee Name : Manu,ID:11123
obj2.displayWorkingHours()#Company Name : UST,weekly Working Hour : 45
print(obj2.maximumOfTwoNum(2,4))#4
