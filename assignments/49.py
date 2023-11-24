'''Write a program to find out big of two numbers'''
num1, num2 = map(int,input("Enter your numbers here : ").split())
if num1 > num2:
    print(f"{num1} is biggest number")
elif num1<num2:
    print(f"{num2} is biggest number")
else:
    print("Both are equal")