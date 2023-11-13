def func(name, age, aadhar=None, phone=None, **kwargs):
    print('name- ', name)
    print('age-', age)

    if 'email' in kwargs:
        print("Email is not mandatory field")

    if aadhar is not None:
        print('aadhar is not mandatory field')

    if phone is not None:
        print('phone -',  phone)

    
try:       
    func(40, phone='9849123459', email = 'raju@gmail.com',aadhar='872541477779')
    print()
    
except:
    if name not in kwargs:
        print('name is mandatory') 
    elif age not in kwargs:
        print('age is mandatory')
    else:
        print('age and name are mandatory')

