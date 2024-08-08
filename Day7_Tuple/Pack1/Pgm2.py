#Tuple - Read only version of list
a=()
print(type(a))#<class 'tuple'>
b=(12)
print(type(b))#<class 'int'>
c=(12,)
print(type(c))#<class 'tuple'>
print(c)#(12,)
#c.append(13)#AttributeError: 'tuple' object has no attribute 'append'
print(c[0])#12
#c[0]=30#TypeError: 'tuple' object does not support item assignment
#del c[0]#TypeError: 'tuple' object doesn't support item deletion
del c
#print(c)#NameError: name 'c' is not defined
