''' BMI calculation: take required parameters for BMI calculation from the user and calculate BMI of the person.'''
KG = float(input("Enter your weight in KG : "))
Height = float(input("Enter your weight in meters : "))

BMI = KG/(Height**2)

print(f"Your BMI is {BMI}")