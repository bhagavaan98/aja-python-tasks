'''print the number in proper mathematical way. 
Consider that we have 6 digit numbers. 
Number format  WAP> 10 -> 000010 
100 ->  000100 
1000 ->  001000 
2345678  ->  2345678 
If the number has more than 6 digits then print as it is.'''
num = input("Enter your number here : ")
if len(num) < 6:
    ans = 6-len(num)
    ans1 = ans*"0"
    print(ans1+num)
else:
    print(num)
