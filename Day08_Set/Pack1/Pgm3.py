a={12,34,56,78,12}
a.add(99)
print(a)#{34, 99, 12, 78, 56}
a.add(99)
print(a)#{34, 99, 12, 78, 56}
#a.add(22,34,56)#TypeError: set.add() takes exactly one argument (3 given)
#a.update(12,13)#TypeError: 'int' object is not iterable
a.update([12,32],(11,),"Hello",{1,2,3})
print(a)#{32, 1, 34, 99, 'e', 2, 3, 'o', 11, 12, 78, 'H', 'l', 56}

