#Slicing
#Syntax -> value(start index:end index:step)
#end index will not be included, slicing will not go after end index
#space will be included as a charactor
name="Python programming"
print(name[4:6:1])#end index is not included
print(name[::])#start and end will take automatically
print(name[:])#first and last
print(name[1:])#get the last charactor
print(name[-4:])
print(name[4::-1])# reverse direction
print(name[4::-2])
print(name[::-1])#reverse order of whole string

