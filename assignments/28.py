'''take a number from the user and check whether it is prime?'''
Num  = int(input("Enter your number here : "))
if Num <=1 :
    print(f"This is not a prime number {Num}")
elif Num >= 2:
    Num1 = Num//2
    for i in range(2,Num1):
        if Num%i == 0:
            print(f"This is not a prime number {Num}")
            break
    else:
        print("This is a prime number")
