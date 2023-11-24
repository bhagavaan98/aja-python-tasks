'''take a string from the user and check contains only  small letters or not? '''
string = input("Enter your string here : ")
if string.islower():
    print("This only contains small letters")
else:
    print("This does not contains all the small letters")