'''take a string from the user and check contains only  small letters or not'''
string = input("Enter the string here : ")
for i in string:
    if not i.isalpha() and not i.islower():
        print("The given string contains more than lower letters")
        break    
else:
    print("The given string contains only lower letters")
