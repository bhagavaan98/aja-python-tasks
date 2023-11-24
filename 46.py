'''Play a number guessing game (User enters a guess, you print YES or Higher or Lower). 
This should continue until and until user gives a correct number or want to quit in the middle. 
Get a hidden number by using random.randint(1,100)'''
import random

while True:
    Num = int(input("Enter anyone number from 1 to 100 here : "))
    if Num < 1 or Num > 100:
        print("Invalid input. Please enter a number between 1 and 100.")
        continue
    ran = random.randint(1,100)
    if Num == ran:
        print("You have gussed it correct")
        break
    elif Num > ran:
        print("You have gussed it higher")
    elif Num < ran:
        print("You have gussed it lower")
    quit1 = input("Do you want to quit : YES or NO \n").lower()
    if quit1 == "yes":
        break
    

         

