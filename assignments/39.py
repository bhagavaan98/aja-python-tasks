'''take a string from the user and check contains at least one digit or not? '''
String = input("Enter your String here : ")
for i in String:
    if i.isdigit():
        print("This string contains atleast one digit")
        break 
else:
    print("This does not even contain one digit")