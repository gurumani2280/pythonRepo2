x=[2,5,7,4,9]
#x.remove(3)#ValueError: list.remove(x): x not in list
x.remove(7)
print(x)#[2, 5, 4, 9]
x.pop()
print(x)#[2, 5, 4]
x.pop()
print(x)#[2, 5]
x.pop(0)
print(x)#[5]
#x.pop(3)#IndexError: pop index out of range
y=[2,4,3,8,21]
y.clear()
print(y)#[]
z=[21,34,67,8]
#z.clear(1)#TypeError: list.clear() takes no arguments (1 given)
del z[2]
print(z)#[21, 34, 8]
del z
#print(z)#NameError: name 'z' is not defined
a=[2,34,56,78,52,61,75]
#del a[0,2]#TypeError: list indices must be integers or slices, not tuple
del a[1:7:2]
print(a)#[2, 56, 52, 75]

