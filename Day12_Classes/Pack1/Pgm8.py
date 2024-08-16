class Employee:
    companyName="UST"
    def __init__(self,name,id):
        print("constructor - it will get executed automatically whenever we create object for the class")
        self.name=name
        self.id=id

    def printEmployeeDetails(self):#self in argument for any method inside any class, which means it is a instance class
        print(f"Company Name: {self.companyName},Employee Name : {self.name},ID:{self.id}")
obj1=Employee("Aby",10234)
obj1.printEmployeeDetails()#Company Name: UST,Employee Name : Aby,ID:10234
obj2=Employee("Manu",11123)
obj2.printEmployeeDetails()#Company Name: UST,Employee Name : Manu,ID:11123
