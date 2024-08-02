# Get the sum of numbers from 1-10
a=1
b=int(input("Enter the number :"))
sum=0
while a<=b:
    sum=sum+a
    a=a+1
else:
    print("condition has become false",a)
print(f"sum of the value is {sum}")
sum_using_formula=(b*(b+1))//2
print(sum_using_formula)
