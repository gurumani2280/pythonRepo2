#int conversion
a=True
print(int(a))#1
print(int(False))#0
"""int conversion for boolean value True will return 1
False value will return 0
"""
b=10.5
print(int(b))#10
"""For Float value int function will return the integer/non decimal part
Decimal part will be ignored.
"""
c="5"
print(int(c))
#print(int("test1"))# ValueError: invalid literal for int() with base 10: 'test1'
#print(int("1.2"))#ValueError: invalid literal for int() with base 10: '1.2'
#print(int(""))#ValueError: invalid literal for int() with base 10: ''
""" For a string value int() will check the content within the given string
If the content is int then int() able to convert to int, otherwise it throws error.
"""
