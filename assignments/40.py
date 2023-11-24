'''take a string from the user and check contains at least one alphabets or not? '''
String = input("Enter your String here : ")
for i in String:
    if i.isalpha():
        print("This string contains atleast one alphabet")
        break 
else:
    print("This does not even contain one alphabet")