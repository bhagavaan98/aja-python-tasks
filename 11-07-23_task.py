def func(name, age, aadhar=None, phone=None, **kwargs):
    print('name- ', name)
    print('age-', age)

    if 'email' in kwargs:
        print("Email is an extra field")

    if aadhar is not None:
        print('aadhar is extra field', aadhar)

    if phone is not None:
        print('phone -',  phone)

    
try:       
    func('alex', 30, phone='1234567890', email = 'a@gmail.com')
    print()
    func( phone='1234567890', email = 'a@gmail.com')
    print()
except:
    print('age and name are mandatory')
