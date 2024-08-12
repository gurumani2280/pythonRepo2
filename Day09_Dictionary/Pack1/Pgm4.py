a={"A":"Apple","B":"Banana",1:"one"}
a.update({"M":"Mango"})
print(a)#{'A': 'Apple', 'B': 'Banana', 1: 'one', 'M': 'Mango'}
a.update({"M":"Orange"})
print(a)#{'A': 'Apple', 'B': 'Banana', 1: 'one', 'M': 'Orange'}
a[4]="Four"
print(a)#{'A': 'Apple', 'B': 'Banana', 1: 'one', 'M': 'Orange', 4: 'Four'}
a.update({"C":"Cat"})#{'A': 'Apple', 'B': 'Banana', 1: 'one', 'M': 'Orange', 4: 'Four', 'C': 'Cat'}
print(a)
print(a.keys())#dict_keys(['A', 'B', 1, 'M', 4, 'C'])
print(a.values())#dict_values(['Apple', 'Banana', 'one', 'Orange', 'Four', 'Cat'])
print(a.items())#dict_items([('A', 'Apple'), ('B', 'Banana'), (1, 'one'), ('M', 'Orange'), (4, 'Four'), ('C', 'Cat')])


