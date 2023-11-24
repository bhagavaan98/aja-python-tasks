'''take a string from the user and check contains at least one capital letter or not'''
String = input("Enter your String here : ")
for i in String:
    if i.isupper():
        print("This string contains atleast one capital letter")
        break 
else:
    print("This does not even contain one capital letter")
    