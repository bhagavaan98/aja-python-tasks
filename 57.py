'''Take a two numbers from the user and do below menu driven operations 
1. addition 
2. multiples 
3.division 
4.sqrt 
5. pow    a**b 
6.subtraction   
After selection do the corresponding operation. 
Note: user may give int, or float numbers. 
You should check whether it is proper digits or not. 
I.e the user given string should be in the position to convert to float. O
ther wise show the “inproper string given” Error. '''
from math import sqrt
num1, num2 = input("Enter your numbers here : ").split()
if num1.isdigit() and num2.isdigit():
    num3 = int(num1)
    num4 = int(num2)
print(num3+num4)
print(num3*num4)
print(num3/num4)
print(sqrt(num3),sqrt(num4))
print(num3**num4)
print(abs(num3-num4))
    