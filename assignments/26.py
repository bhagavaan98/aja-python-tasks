'''Take two number a,b from the user and check whether a is divisible by b or not '''
a,b = map(int,input("Enter the two numbers here : ").split(","))
if a%b == 0:
    print("a is divisible by b")
else:
    print("a is not divisible by b")