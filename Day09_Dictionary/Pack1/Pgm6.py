a={"A":"Apple","B":"Banana","C":"Cat",1:"one",2:"Two"}
for i in a:
    print(i,end=",")#A,B,C,1,2,->Printing Keys
print()
for i in a.keys():
    print(i,end=",")#A,B,C,1,2,
print()
for i in a.values():
    print(i, end=",")#Apple,Banana,Cat,one,Two,
print()
for i in a.items():
    print(i, end=",")#('A', 'Apple'),('B', 'Banana'),('C', 'Cat'),(1, 'one'),(2, 'Two'),

