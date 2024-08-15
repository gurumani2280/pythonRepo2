#Keyword variable length argument
def user_data(**data):
    print(data)#{'name': 'python', 'id': '111', 'phone': 889299}
    print(type(data))#<class 'dict'>
user_data(name="python", id="111",phone=889299)