'''define a function to take person details name and age are mandatory parameters and height weight are optional parameters. 
If the user willing to pass any other details(like adhar, cell, pan, passport etc..) 
regarding him then your function should access those details.'''
def person_details(name,age,height= None,weight=None,**kwargs):
    print(f"Name is : {name}")
    print(f"Age is : {age}")
    
    if height is not None:
        print(f"Height is : {height}")
    if weight is not None:
        print(f"Weight is : {weight}")
    for key, value in kwargs.items():
        print(f"{key}:{value}")

person_details("Alice", 35, adhar="1234 5678 9012", cell="9876543210", pan="ABCDE1234F")
