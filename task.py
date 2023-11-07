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
    func('raju', 30, phone='56854854555', email = 'raj@gmail.com')
    print()
    func( phone='56854854555', email = 'raj@gmail.com')
    print()
except:
    print('age and name are mandatory')
