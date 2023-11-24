'''take a string from the user and check contains only  special chars or not'''
string = input("Enter your string here : ")
count = 0
for i in string:
    if not i.isalnum():
        count +=1
if count == len(string):
    print("This contains only special chars")
else:
    print("This contains more than special chars")
