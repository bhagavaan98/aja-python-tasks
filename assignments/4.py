'''take four numbers from the user (variables name it as x1,x2,x3,x4) 

 Do the below operations 

 (x1+x2)**2, (x3+x4)**3 

variance 

standard deviation: sqrt(variance):  User math module. Math.sqrt(variance) 

Regression 

y=mx+b 

          m=1.23 

          b=0.045 

          find out y 

          y=m*(x1+x2+x3+x4)+b 

 Find the average of four numbers 

Find the sum of four numbers   
'''
import math
x1 = int(input("Enter the number : "))
x2 = int(input("Enter the number : "))
x3 = int(input("Enter the number : "))
x4 = int(input("Enter the number : "))

ans1 , ans2 = (x1+x2)**2 , (x3+x4)**3
print(ans1,ans2)
mean = (x1+x2+x3+x4)/4
variance = (((x1-mean)**2) + ((x2-mean)**2) + ((x3-mean)**2) + ((x1-mean)**2))/4
standard_deviation = math.sqrt(variance)
Regression = 1.23*(x1+x2+x3+x4)+0.045
Avg = (x1+x2+x3+x4)/4
Sum = x1+x2+x3+x4

print(Sum)
print(Regression)
print(Avg)
print(standard_deviation)
print(variance)