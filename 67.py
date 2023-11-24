'''write a function to check given value is prime or not '''
def fun(prime):
    if prime<= 1:
        print(f"This is not a Prime number{prime}")
    else:
        for i in range(2, prime):
            if prime%i == 0:
                print(f"This is not a prime number {prime}")
                break
        else:
            print(f"This is a prime number {prime}")

fun(97)