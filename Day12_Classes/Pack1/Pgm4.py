class Dog:
    legs=4
    def __init__(self):
        print("Creating objects for Dogs class")
        self.color="White"#It is an instance variable, bcz we use self reference variable to create
obj1=Dog()#Creating objects for Dogs class
print(obj1.legs)#4
print(obj1.color)#White
obj2=Dog()#Creating objects for Dogs class
print(obj2.legs)#4
print(obj2.color)#White



