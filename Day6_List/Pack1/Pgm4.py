x=[1,2,3]
print(x[0])#1
x[0]=5
print(x[0])#5
#x[3]=5#IndexError: list assignment index out of range
x.append(6)
print(x)#[5, 2, 3, 6]
print(x[3])#6
#x.append(3,6,8)#TypeError: list.append() takes exactly one argument (3 given)
#x.insert(56)#TypeError: insert expected 2 arguments, got 1
x.insert(5,20)#[5, 2, 3, 6, 20]
print(x)
x.insert(2,11)
print(x)#[5, 2, 11, 3, 6, 20]
x.insert(-2,90)
print(x)#[5, 2, 11, 3, 90, 6, 20]
x.insert(-20,55)
print(x)#[55, 5, 2, 11, 3, 90, 6, 20]