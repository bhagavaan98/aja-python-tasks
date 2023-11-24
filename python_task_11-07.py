l = ['a', 'b', 'c', 'a', 'b', 'a', 'c', 'a', 'b']
t = input('enter a target charcter to change last 2 occurences: ')
c = l.count(t)
x=[]
coun=0
for i in l:
    if i == t:
        coun+=1
        if coun > (c-2):
            x.append(i.upper())
        else :
            x.append(i)
    else :
        x.append(i)
print(x)








##def Employee(name, age, aadhar=None, phone=None, **kwargs):
##    print('name- ', name)
##    print('age-', age)
##
##    if 'email' in kwargs:
##        print("Email is an extra field")
##
##    if aadhar is not None:
##        print('aadhar is extra field', aadhar)
##
##    if phone is not None:
##        print('phone -',  phone)
##
##    
##try:       
##    Employee('gowardhan', 50, phone='9955668877', email = 'a@gmail.com')
##    print()
##    Employee( phone='9898567890', email = 'hjja@gmail.com')
##    print()
##except:
##    print('age and name are mandatory')
