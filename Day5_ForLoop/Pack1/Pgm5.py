a=["Apple","Mango","Orange","Grape","Banana",40,1,30,11,100]
for item in a:
    print(type(item))
    print(str(type(item)) == "<class 'str'>")
    if str(type(item)) == "<class 'str'>":
        for c in item:
            print(c)
    else:
        print("Not a string")