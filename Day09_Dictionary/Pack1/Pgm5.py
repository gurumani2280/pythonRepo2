a={"A":"Apple","B":"Banana",1:"one",2:"Two"}
del a[1]
print(a)#{'A': 'Apple', 'B': 'Banana'}
#del a[1]#KeyError: 1
a.pop("B")
print(a)#{'A': 'Apple'}
print(a)
a.__delitem__("A")
print(a)#{2: 'Two'}
a.popitem()
print(a)#{}

