'''take a string from the user and check contains only  special chars or not'''
string = input("Enter the string here : ")
for i in string:
    if i.isalnum():
        print("The given string contains more than special chars")
        break
else:
    print("The given string contains only special chars")