'''input: "Google" print count of each character'''
string = input("Enter your string here : ")
x = set(string)
for i in x:
    print(f"The count of {i}",string.count(i))
    