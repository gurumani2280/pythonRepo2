class Employee:
    companyName="UST"
    def __init__(self,name,id):
        print("constructor - it will get executed automatically whenever we create object for the class")
        self.name=name
        self.id=id
obj1=Employee("Aby",10234)
print(obj1.companyName)#UST
print(obj1.name)#Aby
print(obj1.id)#10234
obj2=Employee("Manu",11123)
print(obj2.companyName)#UST
print(obj2.name)#Manu
print(obj2.id)#11123