'''take a string from the user and check contains only digits or not? '''
string = input("Enter your string here : ")
if string.isdigit():
    print("contains only digits")
else:
    print("Its contains more than digit")