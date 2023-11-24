'''Convert every word start letter into caps. 
Some how title not working if it contains numbers and special symbols in the word'''
string = input("Enter the string here : ").split()
for i in string:
    if not i.isalpha():
        print("Title does not work for the strings with ")