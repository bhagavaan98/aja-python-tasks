'''Determine the factors of a number entered  by the user'''
Num = int(input("Enter your number here : "))
for i in range(1,Num):
    if Num%i == 0:
        print(f"factor of a number entered is {i}")