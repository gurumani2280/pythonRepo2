"""Create a function which takes 2 arguments and returns sum,differnce,
multiply,division,remindor,power"""
def program(a,b):
    print(f"Function program with arguments:{a,b}")#Function program with arguments:(2, 3)
    return a+b,a-b,a*b,a/b,a%b,a**b
print(program(2,3))#(5, -1, 6, 0.6666666666666666, 2, 8)
c=program(3,4)
print(c)#(7, -1, 12, 0.75, 3, 81)
print(type(c))#<class 'tuple'>#if returning multiple args the type will be tuple
print(program(b=5,a=3))#Function program with arguments:(3, 5) (8, -2, 15, 0.6, 3, 243)
print(program(a=3,b=5))#Function program with arguments:(3, 5)  (8, -2, 15, 0.6, 3, 243)
#program()#TypeError: program() missing 2 required positional arguments: 'a' and 'b'

