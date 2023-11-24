'''Take a letter from the user and print that letter belongs to which category 
I.e is it a small letter or capital letter or number or special symbol'''
letter = input("Enter the letter here : ")
if letter.isupper():
    print("it is captial")
elif letter.islower():
    print("it is small")
elif letter.isdigit():
    print("it is number")
else:
    print("it is a special symbol")