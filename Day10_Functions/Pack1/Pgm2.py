# Create a function which takes two integer argument and returns some of the provided argument
def add(a,b):
    print("inside add function with arguments",a,b)
    return a+b
x=add(5,10)#inside add function with arguments 5 10
y=add(1,2)
print(y)
print(x)
print(add(5,5))
print(add(input("please enter first Num:"),input("Please enter the second Num: ")))#10+10 -> 1010
print(add(int(input("please enter first Num:")),int(input("Please enter the second Num: "))))#1+12 -> 13

