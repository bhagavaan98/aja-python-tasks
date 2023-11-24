'''take a string from the user and check contains at least one small letter or not'''
String = input("Enter your String here : ")
for i in String:
    if i.islower():
        print("This string contains atleast one small letter")
        break 
else:
    print("This does not even contain one small letter")
    