class Person:
    country="India"
    def __init__(self,name):
        self.name=name
print(Person.country)#India
Person.country="Bharat"
print(Person.country)#Bharat
person1=Person("Manu")
print(person1.country)
print(person1.name)#Manu
person2=Person("Binu")
print(person2.country)#Bharat
print(person2.name)#Binu


