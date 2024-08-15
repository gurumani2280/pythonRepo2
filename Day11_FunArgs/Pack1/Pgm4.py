#Create a fun which takes variable length arguments and it rerurn sum of all the arguments
def sum(*num,a):#'*' indicates variable length argument
    print(num)
    print(type(num))
    sum1=0
    for i in num:
        sum1=sum1+i
    return(sum1)
#print(sum())#TypeError: sum() missing 1 required keyword-only argument: 'a'
#print(sum(5))#TypeError: sum() missing 1 required keyword-only argument: 'a'
#print(sum(5,4))#TypeError: sum() missing 1 required keyword-only argument: 'a'
#print(sum(5,4,3))#TypeError: sum() missing 1 required keyword-only argument: 'a'
print(sum(1,2,a=3))#3