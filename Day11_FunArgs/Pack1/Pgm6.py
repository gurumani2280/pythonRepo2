def person_details(*a,**b):
    print(a)#()
    print(type(a))#<class 'tuple'>
    print(b)#{}
    print(type(b))#<class 'dict'>
person_details()
person_details(name="Apple")
"""
<class 'tuple'>
{'name': 'Apple'}
<class 'dict'>
"""
person_details("Apple")
"""
{}
<class 'dict'>
"""
person_details("apple",name="Android")
"""
('apple',)
<class 'tuple'>
{'name': 'Android'}
<class 'dict'>
"""