'''Given an age, figure out whether someone's a baby, toddler, child, teenager, adult or old codger. '''
Age = int(input("Enter you age here : "))
if Age > 0 and Age <= 1:
    print("You are a baby")
elif Age > 1 and Age <= 3:
    print("You are a toddler")
elif Age > 3 and Age <= 12:
    print("You are a child")
elif Age > 12 and Age <=17:
    print("You are a teenager")
elif Age > 17 and Age <= 60:
    print("You are a Adult")
elif Age > 60:
    print("You are a old codger")
else: 
    print("Error : enter the correct value ")
