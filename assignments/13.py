'''Assign “ten” value to variable it is 10 otherwise assign “Not ten” 

       Note: write two versions of program 

Version1: use and operator 

Version2: use or operator  '''
Num = int(input("Enter the number here : "))
if Num == 10:
    print(Num or 10)
else:
    print("Not Ten")

if Num == 10:
    print (Num and 10)
else:
    print("Not Ten")