class Employee:
    companyName="UST"
    def __init__(self):#constructor - it will get executed automatically whenever we create object for the class
        print("constructor - it will get executed automatically whenever we create object for the class")
obj1=Employee()#constructor - it will get executed automatically whenever we create object for the class
print(obj1)#<__main__.Employee object at 0x000001FFA4097DA0>
print(type(obj1))#<class '__main__.Employee'>
print(obj1.companyName)#UST