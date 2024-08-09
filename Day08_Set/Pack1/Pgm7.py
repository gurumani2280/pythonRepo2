a={1,2,3,4,5,6}
b={4,5,6,7,8}
print(a.intersection(b))#{4, 5, 6}
print(a.union(b))#{1, 2, 3, 4, 5, 6, 7, 8}
print(a.difference(b))#{1, 2, 3}
print(a.symmetric_difference(b))#{1, 2, 3, 7, 8}
print(a & b)#{4, 5, 6} &->intersection
print(a | b)#{1, 2, 3, 4, 5, 6, 7, 8} |-> union
print(a ^ b)# {1, 2, 3, 7, 8} ^ -> symmetric_difference
print(a - b)#{1, 2, 3} - -> difference
