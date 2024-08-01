#Float conversion
a=True
print(float(a))#1.0
print(float(False))#0.0
"""Float conversion for boolean value True will return 1.0
False value will return 0.0
"""
print(float(15))#15.0
"""For int value float() will return the integer with decimal part
"""
print(float("1"))#1.0
#print(float("Test"))#ValueError: could not convert string to float: 'Test'
""" For a string value float() will check the content within the given string
If the content is int/float then float() able to convert to float, otherwise it throws error.
"""
