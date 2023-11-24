'''take a string from the user and check contains only  alphabets or not?'''
string = input("Enter the string here : ")
for i in string:
    if not i.isalpha():
        print("The given string contains more than alphabets")
        break
else:
    print("The given string contains only alphabets")
