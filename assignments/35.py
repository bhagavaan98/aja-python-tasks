'''WAP to check given string contains numbers or not. it should consider float numbers also. '''
string = input("Enter your string here : ")
for i in string:
    if i.isnumeric or i == '.':
        print("This String contains Numbers")
        break
else:
    print("This does not contains numbers")
