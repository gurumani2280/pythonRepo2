#Accessing dictionary value based on the key
a={"A":"Apple","B":"Banana",1:"one"}
print(a[1])#one
print(a["A"])#Apple
#print(a[5])#KeyError: 5
#print(a[1],a["B"])
print(a.get(1))#one
print(a.get(9))#None
print(a.get(5,7))##if key is not available instead of NONE it will give 2nd arg
print(a.get(1,9))#one
print(a.get(7,"it will take 2 nd arg"))#it will take 2 nd arg

