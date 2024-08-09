#a=set(12,34,12)#TypeError: set expected at most 1 argument, got 3
#a=set(12)#TypeError: 'int' object is not iterable
a=set("Hello")
print(a)#{'e', 'o', 'l', 'H'}
print(len(a))#4
print("o" in a)
b=set([11,22,33,44,11])
print(b)#{33, 11, 44, 22}
c=set((11,23,45,67,88,23))
print(c)#{67, 11, 45, 23, 88}
d=set(range(1,10,2))
print(d)#{1, 3, 5, 7, 9}
e=set({1, 3, 5, 7, 9})
print(e)#{1, 3, 5, 7, 9}
f=e.copy()
print(f)
