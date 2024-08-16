class Person:
    country="India"#It is created directly,so it a static/class variable
print(Person.country)#India
Person.country="Bharat"
print(Person.country)#Bharat
person1=Person()
print(person1.country)#Bharat
#Class variables belongs to all the objects
person1.name="Tintu"
"""This name attribute is an instance/objects variable, because use reference variable to create this name 
variable"""
print(person1.name)#Tintu
person2=Person()
print(person2.country)#Bharat
#print(person2.name)#AttributeError: 'Person' object has no attribute 'name'
person2.name="Pintu"
print(person2.name)#Pintu


