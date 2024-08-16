class Dog:
    legs=4
    def __init__(self,color):#color->Local variable to constructor
        print("Creating objects for Dogs class",color)
        self.color=color#self.color -> instance variable, color -> Local variable
#obj1=Dog()#TypeError: Dog.__init__() missing 1 required positional argument: 'color'
obj1=Dog("Red")#Creating objects for Dogs class Red
print(obj1.legs)#4
print(obj1.color)#Red
obj2=Dog("Blue")#Creating objects for Dogs class Blue
print(obj2.legs)#4
print(obj2.color)#Blue



