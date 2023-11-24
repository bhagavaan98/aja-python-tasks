'''Take name, age, height from the user and print like below 

The details of the person: Name:name of the person, Age:age of the person, Height:height of the person 

Note: make sure that no space between : and a value and should be space after “COMA” '''

name = input("Enter you name : ")
age = int(input("Enter your age : "))
height = float(input("Enter your height : "))

print(f"The details of the person: Name:{name}, Age:{age} of the person, Height:{height} of the person")
