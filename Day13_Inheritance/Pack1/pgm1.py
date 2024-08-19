class A:
    def __init__(self):
        print("No argument constructor")

    def __init__(self,a):
        print("It's argument constructor")
#obj1=A()#A.__init__() missing 1 required positional argument: 'a'
#in python we can create multiple method, but it will take the last one
obj2=A(10)#It's argument constructor