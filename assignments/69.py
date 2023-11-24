'''take a string from the user and check contains only digits or not?'''
string = input("Enter the string here : ")
for i in string:
    if not i.isdigit():
        print("The given string contains more than digit")
        break
else:
    print("The given string contains only digit")
