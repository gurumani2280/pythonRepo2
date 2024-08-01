#Boolean conversion
a=10
b=bool(a)
print(b)#True
a1=0
b1=bool(a1)
print(b1)#false
print(bool(10.5),bool(0.0))#True False
print(bool("abc"),bool(""))#True False
"""bool()will convert any data type to boolean
For int value=0 bool function will give false
For non 0 value it will return True
For float 0.0 will return false
All other value will return false
Empty string("") it will return false
For any other string value it will return true
"""