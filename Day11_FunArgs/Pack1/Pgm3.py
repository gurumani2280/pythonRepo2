#Create a fun which takes variable length arguments and it rerurn sum of all the arguments
def sum(*num):#'*' indicates variable length argument
    print(num)
    print(type(num))
    sum1=0
    for i in num:
        sum1=sum1+i
    return(sum1)
print(sum())#output -> 0
print(sum(5))
print(sum(5,4))
print(sum(5,4,3))