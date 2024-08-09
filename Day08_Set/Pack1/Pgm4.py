a={1,2,3,4,5,6,7,1}
a.remove(2)
print(a)#{1, 3, 4, 5, 6, 7}
#a.remove(2) # KeyError: 2
a.pop()
print(a)#{3, 4, 5, 6, 7}
a.pop()
print(a)#{4, 5, 6, 7}
a.discard(5)
print(a)#{4, 6, 7}
a.discard(5)
print(a)#{4, 6, 7}
a.clear()
print(a)# set()
#a.pop()#KeyError: 'pop from an empty set'
