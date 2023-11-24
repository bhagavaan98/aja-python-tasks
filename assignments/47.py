'''Take two numbers from the user a,b check whether a is divisible by b or not?'''
num1, num2 = map(int,input("Enter your numbers here : ").split())
if num1%num2 == 0:
    print("a is divisible by b")
else:
    print("a is divisible not by b")