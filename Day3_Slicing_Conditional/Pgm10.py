list1= ["zero","one","two","three","four","five"]
num1=int(input(f"Please enter a valid number btw 0 and {len(list1)-1}"))
#f string, if we want to 
print(len(list1))
if num1 < len(list1):
    print(list1[num1])
else:
    print(f"Please enter a valid number btw 0 and {len(list1)-1}")

