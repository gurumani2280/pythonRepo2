"""For Loop
Syntax :
for  <item> in <String/list/range..>:
    <Statement>
"""
fruits=["Apple","Mango","Orange","Grape","Banana"]
print(type(fruits))
for fruit in fruits:
    print("Fruit is",fruit)
    print("Count of char in fruit",len(fruit))
    print("First letter of the fruit is",fruit[0])
else:
    print("All the fruit in the list is printed")
