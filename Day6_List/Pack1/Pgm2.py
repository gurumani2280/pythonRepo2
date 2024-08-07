x=[1,2,3,4]
print(x)#[1, 2, 3, 4]
print(type(x))#<class 'list'>
y=list([111,34,56,78,34])
print(y)#[111, 34, 56, 78]
print(type(y))#<class 'list'>
print(len(y))#5
print(y[3])#78
#print(y.index(2))#ValueError: 2 is not in list
print(y.index(34))#1
print(y.index(78))#3
print(y.count(111))#1
print(y.count(34))#2
print(y[1:3:2])#34