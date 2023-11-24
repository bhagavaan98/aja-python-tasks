'''code to perform mathematical operations. take two numbers from the user and show the below menu 

1. add, 

2. sub,	 

3. mul, 

 	4.div,  

5.quit 

Enter an option: 

based on the option need to perform an operations'''
Num1, Num2 = map(int,input("Enter the Numbers here : ").split())
Option = int(input("Please select the options.\n1.ADD\n2.SUB\n3.MUL\n4.DIV\n5.QUIT\n"))
if Option == 1:
    print(Num1+Num2)
elif Option == 2:
    print(Num1-Num2)
elif Option == 3:
    print(Num1*Num2)
elif Option == 4:
    print(Num1/Num2)
elif Option == 5:
    exit
