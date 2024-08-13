# Write a function to check if the given number is Even or Odd
def check_even_odd(a):
    print("Check Even Odd function with input",a)
    if a%2==0:
        print(f"The given number {a} is even")
    else:
        print(f"The given number {a} is odd")
#check_even_odd()#TypeError: check_even_odd() missing 1 required positional argument: 'a'
check_even_odd(12)#The given number 12 is even
check_even_odd(int(input("Enter a Num:")))#Num=21, The given number 21 is odd



