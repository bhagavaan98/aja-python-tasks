'''take a string from the user and check contains only  capital letters or not'''
string = input("Enter the string here : ")
for i in string:
    if not i.isalpha() and not i.isupper():
        print("The given string contains more than capital letters")
        break    
else:
    print("The given string contains only capital letters")
