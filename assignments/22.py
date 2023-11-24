'''Take age and gender from the user and decide whether he is eligible for 	marriage in India or not. 

Age criteria: men age>24, women>21 '''

Gender = int(input("Select Your Gender\n1.Man\n2.Woman\n"))
Age = int(input("Enter you age here : "))
if (Gender == 1 and Age > 24) or (Gender == 2 and Age > 21):
    print("You are eligible for marriage in India")
else:
    print("You are not eligible for marriage in India")