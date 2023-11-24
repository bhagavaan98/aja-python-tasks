'''write a function to check given 2 values are  divisible or not '''
def fun(a,b):
    if a%b == 0:
        print(f"{a} is divisible by {b}")
    elif b%a == 0:
        print(f"{b} is divisible by {a}")

fun(9,3)