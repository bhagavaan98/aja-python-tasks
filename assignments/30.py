'''take a string from the user and check contains only  alphabets or not'''
string = input("Enter your string here : ")
if string.isalpha():
    print("contains only alphabets")
else:
    print("Its contains more than alphabets")