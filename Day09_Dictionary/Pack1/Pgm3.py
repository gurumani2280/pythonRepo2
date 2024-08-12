#Find the frequency of each char of the given word
#given word
a="python programming"
d= {}
for i in a:
    value = d.get(i,0)
    d.update({i:value+1})
    print(d)
print(d)


