#!/usr/bin/env python
# coding: utf-8

# In[2]:


'''1.Take the input from the user for(Total number of people,Number of seats for bus. Based on two
inputs
Decide how many number of buses required'''

people = int(input('Enter total no of peoples: '))
seats = int(input('Enter no of seats for each bus: '))

buses = people // seats
if (people // seats) != 0:
    buses += 1
print('No of buses required for {} people with no of seats {} is {}'.format(people, seats, buses))



# In[3]:


'''2.take temperature from the user and convert foreign heat -&gt; Celsius.'''
# c = (fh -32)*5/9
fh = eval(input('enter foreign heat to find celsius: '))
c = (fh -32)*5/9
print(c)


# In[4]:


'''3.take temperature from the user and convert Celsius → foreign heat.'''
#fahrenheit = (celsius * 9 / 5) + 32
ct = float(input('enter celsius to find foreign heat: '))
fh = (ct * 9 / 5) + 32
print(fh)


# In[5]:


'''4.take four number from the user (variables name it as x1,x2,x3,x4)
Do the below operations
(x1+x2)**2, (x3+x4)**3
variance
standard deviation: sqrt(variance): User math module. Math.sqrt(variance)
Regression
y=mx+b
m=1.23
b=0.045
find out y
y=m*(x1+x2+x3+x4)+b
Find the average of four numbers
Find the sum of four numbers'''

from math import *

x1 = int(input('enter x1 value: '))
x2 = int(input('enter x2 value: '))
x3 = int(input('enter x3 value: '))
x4 = int(input('enter x4 value: '))

l = [x1, x2, x3, x4]
op1 = (x1+x2)**2
op2 = (x3+x4)**3

mean = sum(l)/4
varience = sum(i-mean for i in l)/4
standardde = sqrt(varience)

m=1.23
b=0.045
y=m*(x1+x2+x3+x4)+b

avg = sum(l)/len(l)
summ = sum(l)

print('op1 - {}, op2 - {}, mean - {}, varience - {}, standard deviation - {}, y - {}, avg - {}, summ - {}'.format(op1, op2, mean, varience, standardde, y, avg, summ))


# In[7]:


'''5.Take the distance in km
Show that in cm, meters, in milli meters, cents, feets, yards'''

distance_km = eval(input('enter distance_km to fil=nd above all: '))

meters = distance_km * 1000
centimeters = distance_km * 100000
millimeters = distance_km * 1000000
inches = distance_km * 39370.1 
feet = inches / 12
yards = feet / 3


print(meters, centimeters, millimeters, inches,  feet, yards)


# In[10]:


'''6.Take the size of your hard disk in GB
     	Show that in MB, KB, TB, PB
'''
#     gb_to_mb = 1024
#     mb_to_kb = 1024
#     gb_to_tb = 0.001
#     tb_to_pb = 0.000001

gb = int(input('enter how much gb u want to take: '))
mb = gb * 1024
kb = mb * 1024
tb = gb * 0.001
pb = tb * 0.000001
print('mb {}, KB {}, TB {}, PB {}'.format(mb, kb, tb, pb))


# In[12]:


''' 7.  Take name, age, height from the user and print like below
The details of the person: Name:name of the person, Age:age of the person, Height:height of the person
Note: make sure that no space between : and a value and should be space after “COMA”
'''

name = 'alex'
age = 24
height = 5.9
print('Name:{}, Age:{}, Height:{}'.format(name, age, height))


# In[14]:


'''8. BMI calculation: take required parameters for BMI calculation from the user and calculate BMI of the person.'''
weight = float(input('Enter weight in kilograms: '))
height = float(input('Enter height in meters: '))
op = height/(weight**2)
print(op)


# In[21]:


'''9. name="Jayaram"
age=1.6
height=3.5356234
weight=10.343856783
By using above inputs print the output
Name:Jayaram, Age:1.6, Height:3.54, Weight:10.344
Note: Use format specifiers(%s, %d, %f)
'''
name="Jayaram"
age=1.6
height=3.5356234
weight=10.343856783
op = f'Name:%s, Age:%1f, Height:%2f, Weight:%3f' % (name, age, height, weight)
print(op)


# In[22]:


'''10. Take three upper case letters from the user convert in to small case.'''
s = input('enter something in upper case: ')
print(s.lower())


# In[2]:


'''11. take base and exponent value from the user and print like in mathematics:
  example: base=2, exponent=3: 23  Use: 2\u00b3
'''
base = input("Enter base value:- ")
exponent = input("Enter exponent value:- ")
ex = f'base={base}, exponent={exponent}: {base}^{exponent}'
print(ex)


# In[ ]:


'''12. Take some groceries cost prices and print total cost and average cost, what is the max cost, what is the minimum cost.'''

cost_prices = [20,10,30,8,30,33,44,55,9,29]
total_cost = sum(cost_prices)
avg_cost = total_cost / len(cost_prices)
max_cost = max(cost_prices)
min_cost = min(cost_prices)
print("Total cost:-", total_cost)
print("Average cost:-", avg_cost)
print("Max cost:-", max_cost)


# In[4]:


'''13. Assign “ten” value to variable it is 10 otherwise assign “Not ten”
Note: write two versions of program
Version1: use and operator
Version2: use or operator '''



n1= int(input("Enter value: "))
n2 = int(input("enter value: "))
if n1 and n2:
    print("ten", 'version1')
else:
    print("Not ten", 'version1')

if n1 or n2:
    print("ten", 'version2')
else:
    print("Not ten", 'version2')


# In[5]:


'''14.Take number from the user decide whether it is even or odd. '''

n = int(input("Enter a value: "))
if n%2 == 0:
    print("EVEN")
else:
    print("ODD")


# In[ ]:


'''15.take number from the user decide whether it is positive number or negative number '''

n = input()
if n[0] == "-":
    print("Negative number")
else:
    print("Positive number")


# In[6]:


'''16.take a string from the user print the length. if the user not given anything then show an error message '''

s = input("Enter a word: ")
len_s = len(s)
print(len_s) if len_s else "Error"


# In[7]:


'''17.Code to perform mathematical operations. take two numbers from the user and show the below menu
   1. add,
   2. sub,
   3. mul,
   4.div,
   5.quit
  Enter an option:
  based on the option need to perform an operations
'''

num1 = float(input("Enter number1:- "))
num2 = float(input("Enter number2:- "))
print("1. ADD\n2. SUB\n3. MUL\n4. DIV\n5. Quit ")
user = input("Enter an option to perform a operation:- ")

if user == '1':
    print(num1+num2)
elif user == '2':
    print(num1-num2)
elif user == '3':
    print(num1*num2)
elif user == '4':
    print(num1/num2)
else:
    print("You are quited")


# In[8]:


'''18. show the menu:
    1. kids
    2. Men's
    3. Women's
    Show the corresponding message based on the selection.
    Option:1: you are a kid
    2: you are a gentlemen
    3: you are a good women
    Mention error message if the option value >3.'''

print("1. Kids\n2. Men's\n3. Women's")
user = input("Enter an option:- ")
if user == "1":
    print("You are a Kid")
elif user == "2":
    print("You are a gentlemen")
elif user == "3":
    print("You are a good women")
else:
    print("Error")


# In[ ]:


'''19. Write a program to chcek given substring is there in actual string or not?
    example: act="python is a pure object oriented programing language"
    heck whether “pure” is there in act or not.    Note: Use in operator '''

s = input("Enter a string:- ")
sub_string = input("Enter a sub-string:- ")

if sub_string in s:
    print("YES")
else:
    print("NO")


# In[9]:


'''20. Take three numbers from the user and decide which is big '''
v1 = int(input('enter v1 value: '))
v2 = int(input('enter v2 value: '))
v3 = int(input('enter v3 value: '))
big = 0

if v1 > v2 and v1 > v3:
    big = v1
elif v2 > v1 and v2 > v3:
    big = v2
else:
    big = v3
print(big)


# In[13]:


'''21. Take age and gender from the user and decide whether he is eligible for 	marriage in India or not.
Age criteria: men age>24, women>21 '''

age = int(input('enter your age: '))
gen = input('enter your gender in uppercase letters only like MALA/FEMALE: ')

if (gen == 'MALE' and age > 24) or (gen == 'FEMALE' and age > 21):
    print('yes you are eligible for marriage in India')
else:
    print('sorry you are not eligible, wait for some time buddy...')
 
    


# In[18]:


'''Take an age  and gender from the user: and mention that what he/she can 	do in india.
conditions
1. Theatre: 5 for men 7 for women
2. Voting system: 18 for men and women
3. Marriage in india: 23 for men and for women >21
4. For govt jobs: (min:18, max:32)  for men and (min:18, max:34) for 	women
5. For driving licence: (min:18, max:60) for men and women
Eligibility:
1. theatre
			2.  Voting system
			3.  Marriage in india
			4.  For govt obs
			5. For driving licence:
	Enter an option:
		Gender:
			1. men
			2. women
	Enter an option:
		Enter an age of person: '''


gen = input('enter your option men/women: ')

if gen == 'men':
    age = int(input('enter your age: '))
    if age >= 5:
        print('you can do theatre')
    if age >= 18:
        print('you can do voting')
    if age >= 23:
        print('you can do marrige')
    if age>17 and age<33:
        print('you can do govt jobs')
    if age>17 and age<61:
        print('you can do driving licence')
        
if gen == 'women':
    age = int(input('enter your age: '))
    if age >= 7:
        print('you can do theatre')
    if age >= 18:
        print('you can do voting')
    if age >= 21:
        print('you can do marrige')
    if age>17 and age<33:
        print('you can do govt jobs')
    if age>17 and age<61:
        print('you can do driving licence')        
    






# In[19]:


'''23. operating systems:
1.windows
	2.android
	3.mac
Enter an option:

If the user enters 1 then show "Goto first floor and buy windows laptop or mobile"
If the user enters 2 then show "Goto second floor and buy adroid mobiles"
If the user enters 3 then show "Goto third floor and buy mac laptop or iphones"
If the user enters other than 1 or 2 or 3 then show "There is only three floors, please select 1 or 2 or 3" '''

user = int(input("Enter an option: "))
if user == 1:
    print("Goto first floor and buy windows laptop or mobile")
elif user == 2:
    print("Goto third floor and buy mac laptop or iphones")
elif user == 3:
    print("Goto third floor and buy mac laptop or iphones")
else:
    print("There is only three floors, please select 1 or 2 or 3")


# In[20]:


'''24.Given an age, figure out whether someone's a baby, toddler, child, teenager, adult or old codger. '''

age = int(input("Enter your age: "))
if age <= 1:
    print("bady")
elif age > 1 and age <=5:
    print("toddler")
elif age > 5 and age <=12:
    print("Child")
elif age > 13 and age <= 19:
    print("teenage")
elif age > 20 and age <= 34:
    print("adult")
elif age >= 60:
    print("old codger")
else:
    print("Younger")


# In[22]:


'''25.Take two number a,b from the user and check whether a is divisible by b or not '''

a = int(input("Enter a number1: "))
b = int(input("Enter a number2: "))

if b!= 0:
    if a%b == 0:
        print("Yes")
    else:
        print("No")
else:
    print("Zero division error")


# In[ ]:


'''26. Take a letter from the user and print that letter belongs to which category I.e is it a small letter or capital letter
or number or special symbol '''

user = input("Enter any character only once: ")
if user.isupper():
    print("Upper case")
elif user.islower():
    print("Lower case")
elif user.isdigit():
    print("Number")
else:
    print("Special character")


# In[117]:


'''25. Take a number from the user and check whether it is prime? '''

n = int(input("Enter a number:- "))
# c = 0
# if n <= 1:
#     print("Not Prime")
# else:
#     for i in range(1,n+1):
#         if n%i == 0:
#             c += 1
# if c == 2:
#     print("It's Prime")
# else:
#     print("Not Prime")

n = int(input("Enter a number: "))

if n < 1:
    print(n, 'not prime')
else:
    for i in range(2, n):
        if n % i == 0:
            print(n, 'not prime')
            break
    else:
        print(n, 'is a prime')
    


# In[121]:





# In[28]:


'''26. Take a string from the user and check contains only digits or not? '''

s = input("Enter input: ")

if s.isdigit():
    print("Contain only digits")
else:
    print("Does not contain only digits")


# In[29]:


'''27. Take a string from the user and check contains only alphabets or not? '''
s = input("Enter input:- ")

if s.isalpha():
    print("Contains only alphabets")
else:
    print("Does not contains only alphabets")


# In[34]:


'''28. Take a string from the user and check contains only special chars or not? '''

s = input("Enter input:- ")
l = len(s)
for i in s:
    if not i.isalnum():
        l -= 1 
if l == 0:
    print("Contains only speical characters")
else:
    print("Does not contain only special characters")


# In[38]:


'''29.Take a string from the user and check contains only capital letters or not? '''

s = input("Enter input: ")
l = len(s)
for i in s:
    if i.isupper():
        l -= 1 
if l == 0:
    print("Contains only capital letters")
else:
    print("Does not contan only capital letters")


# In[41]:


''' 30.Take a string from the user and check contains only small letters or not? '''

s = input("Enter input: ")
l = len(s)
for i in s:
    if i.islower():
        l -= 1 
if l == 0:
    print("Contains only capital letters")
else:
    print("Does not contan only capital letters")


# In[42]:


'''
31. WAP to replace last n occurrence of give string.
For example:”apple,orange,apple,grape,orange,apple,apple,orange”
source: “apple”
last occurrences: 2
replace with: APPLE
output:”apple,orange,apple,grape,orange,APPLE,APPLE,orange”
'''

s = "apple, orange, apple, grape, orange, apple, apple, orange"
l = s.split(", ")
op = l[::-1]
c = 0
for i in range (len(l[::-1])):
    if op[i] == 'apple':
        op[i] = "APPLE"
        c += 1
        if c == 2:
            break       
        
print(",".join(op[::-1]))  


# In[57]:


'''32. WAP to check given string contains numbers or not. it should consider float numbers also. '''

# s = eval(input("Enter input: "))
# if type(s)==int or type(s)==float:
#     print("String contains number")
# else:
#     print("String does not contains number")    

s = input("Enter input: ")
try:
    op = float(s) or int(s)
    print('The string contains numbers.')
except ValueError:
    print("The string does not contain numbers.")


# In[ ]:


'''33. Convert the total string in to lower case. Without using lower() function.'''

s = input("Enter input: ")
op = ""
for i in s:
    op += chr((ord(i))+32)
print(op)


# In[59]:


'''
35. Show the below menu to the user until and until user select quit and display corresponding os message
      Menu:

        1. windows
        2. Linux
        3. Mac
        4. quit
'''

while True:
    print("\tMenu: \n1.windows\n2.Linux\n3.Mac\n4.quit")
    user = int(input("Enter input:- "))
    if user == 1:
        print("window")
    elif user == 2:
        print("linux")
    elif user == 3:
        print("mac")
    elif user == 4:
        print("quit")
        break
    else:
        print("any of the option")


# In[60]:


'''36. Take a string from the user and check contains at least one digit or not? '''

s = input("Enter input: ")

for i in s:
    if i.isdigit():
        print("String contains atleast one digit")
        break
else:
    print("String does not contains digit")


# In[ ]:


'''37. Take a string from the user and check contains at least one alphabets or not? '''

s = input("Enter input: ")

for i in s:
    if i.isalpha():
        print("String contains atleast one alphabets")
        break
else:
    print("String does not contains atleat one alphabets")


# In[ ]:


# 38. Take a string from the user and check contains at least one chars or not?

s = input("Enter input: ")

if len(s) >= 1:
    print("String contains at least one chars")
else: 
    print("String does not contains at least one chars")


# In[63]:


# 39. Take a string from the user and check contains at least one capital letter or not?

s = input("Enter input:- ")

for i in s:
    if i.isupper():
        print("String contains at least one capital letter")
        break
else:
    print("String does not contains at least one capital letter")


# In[62]:


# 40. Take a string from the user and check contains at least one small letter or not?

s = input("Enter input:- ")

for i in s:
    if i.islower():
        print("String contains at least one lower letter")
        break
else:
    print("String does not contains at least one lower letter")


# In[61]:


# 41. Print the first 100 odd numbers

count = 0
number = 1

while count < 10:
    if number % 2 != 0:
        print(number, end=' ')
        count += 1
    number += 1
    


# In[64]:


# 42. Determine the factors of a number entered by the user

n = int(input('enter some number: '))
for i in range(1, n+1):
    if n%i == 0:
        print(i)


# In[68]:


'''43. Play a number guessing game (User enters a guess, you print YES or Higher or Lower). This
should continue until and until user gives a correct number or want to quit in the middle.
Get a hidden number by using random.randint(1,100)'''

start = 1
end = 100

while True:
    print('(COMPARE YOUR NUM WITH GIVEN NUMBER IF GIVEN NUM IS HIGH PRINT HIGH)')
    result = (start+end)//2
    print(result)
    output = input("type low, high , correct  : ")
    if output == "low":
        start = result
    if output == "high":
        end = result
    if output == "correct":
        print(result)
        break



# In[69]:


#44. Take two numbers from the user a,b check whether a is divisible by b or not?

a=int(input("Enter any number: "))
b=int(input("Enter any number: "))

if a%b == 0:
    print("a is divisible by b")
else:
    print("a is not divisible by b")


# In[70]:


#45. Find the sum of all the multiples of 3 or 5 below 1000

op = 0
for i in range(1,1000):
    if i%3==0 or i%5==0:
        print(i,end=" ")
        op += i
print()
print("The sum of all the multiples of 3 or 5 below 1000 is=",op)


# In[72]:


#46. Write a program to find out big of two numbers

a=int(input("Enter any number: "))
b=int(input("Enter any number: "))
if a>b:
    print("{} is big".format(a))
else:
    print("{} is big".format(b))


# In[73]:


#47. Write a program to find out biggest number in the given numbers.

a=[1, 2, 5, 33, 6, 70, 9, 0, 3, 4]
ma=0
mi = a[0]
for i in a:
    if int(i)>ma:
        ma=i
print("The biggest number in the given numbers is=",ma)
for i in a:
    if int(i)<mi:
        mi=i
print("The smallest number in the given numbers is=",mi)


# In[74]:


#48. find out the index of third occurrence of given substring

s = input("Enter any string: ")
n = 3
print("{}rd occurance of the string={}".format(n,s[n-1]))


# In[75]:


#49. find out the index nth occurrence of given substring

s = input("Enter any string: ")
n=int(input("Enter index number: "))
print("{} occurance of the string is={}".format(n,s[n-1]))


# In[77]:


#50. Take some single digit numbers from the user and findout min, maximum, sum, average

a= 1, 4, 7, 0, 3
op=0
ma=0
mi=a[0]
for i in a:
    op += i
    if int(i)>ma:
        ma=i
    if int(i)<mi:
        mi=i
    avg=op/len(a)
print("The sum of given numbers are=",op)
print("The maximum number of the given number is=",ma)
print("The minimum number of the given number is=",mi)
print("The average value of the given numbers is=",avg)


# In[101]:


'''51. print the number in proper mathematical way.
	Consider that we have 6 digit numbers.
Number format  WAP> 10 -> 000010
       		100 ->  000100
      		1000 ->  001000
 		 2345678  ->  2345678
'''
n = int(input('enter some number: '))
res = str(n).zfill(6)
print(res)


# In[103]:


'''52. names  ="emp1,emp2,emp3,emp4" iterate through the employee names.'''
names = "emp1,emp2,emp3,emp4"
for i in names.split(','):
    print(i)


# In[104]:


'''53. Take actual string, source string, destination string. replce first nth occurrences of source string
with destination string of actual string.'''

act = 'happynewyear'
sou = 'happy'
occ = int(input('enter some noccurence  count: '))
des = sou + act[(occ+1):]
print(des)
                


# In[107]:


'''54. Take a two numbers from the user and do below menu driven operations
1. addition
2. multiples
3.division
4.sqrt
5. pow a**b
6.subtraction
After selection do the corresponding operation.'''
a = int(input('enter value of a: '))
b = int(input('enter value of b '))
print('addition - {}, multiples - {}, division - {}, sqrt - {}, pow a**b - {}, subtraction - {}'.format(
    a+b, a*b, a//b, (a*a, b*b), a**b, a-b))


# In[110]:


#55. Take numbers from the user and find out min, maximum, sum, average

a=[int(i) for i in input("Enter any numbers: ").split(' ')]
ma=0
mi=a[0]
summ=0
for i in a:
    if i>ma:
        ma=i
    elif i<mi:
        mi=i
    summ +=i
    avg=summ/len(a)
print("The maximum value of the given numbers are=",ma)
print("The minimum value of the given numbers are=",mi)
print("The sum of the given list is=",summ)
print("The average value of the given list is=",avg)


# In[111]:


'''56. l=[1,2,3,5,7,8,9,10,11,12,13,20,22,23,24,25,26,27,20,21,22,4] 
find out how many even numbers are there and how many odd numbers are there
and how many positive numbers are there and how many negative numbers are there 
and how many prime numbers are there and how many perfect numbers are there and 
how many Armstrong numbers are there and how many palindrome numbers are there.'''

l = [1,2,3,5,7,8,9,10,11,12,13,20,22,23,24,25,26,27,20,21,22,4]
even=0
odd=0
positive=0
negative=0
prime=0
summ=0
perfect=0
armstrong=0
palindrome=0
for i in a:
    if i%2==0:
        even += 1
    else:
        odd += 1
    if i>0:
        positive += 1
    else:
        negative += 1
    if i>1:
        for j in range(2,i//2):
            if i%j==0:
                break
        else:
            prime +=1
    summm=0
    for j in range(1,i):
        if j%i==0:
            summm +=i
    if i==summm:
        perfect +=1
    p=len(str(i))
    summ=0
    for j in str(i):
        summ=summ+int(j)**p
    i=int(i)
    if(i==summ):
        armstrong +=1
    if str(i)==str(i)[::-1]:
        palindrome +=1
print("The no of even numbers are=",even)
print("The no of odd numbers are=",odd)
print("The no of positive numbers are=",positive)
print("The no of negative numbers are=",negative)
print("The no of prime numbers are=",prime)
print("The no of perfect numbers are=",perfect)
print("The no of armstrong numbers are=",armstrong)
print("The no of palindrome numbers are=",palindrome)



# In[ ]:


'''57. Take a string from the user and find out how many digits are there, how many special
symbols are there, how many small letters are there, how many caps are there. '''

a=input("Enter any string that should contain digits,symbols,small case and upper case letters: ")
digits=0
special_characters=0
lower_case=0
upper_case=0
for i in a:
    if i.isdigit():
        digits+=1
    elif i.islower():
        lower_case+=1
    elif i.isupper():
        upper_case+=1
    else:
        special_characters+=1
print("no of digits are=",digits)
print("no of special characters are=",special_characters)
print("no of lower case letters are=",lower_case)
print("no of upper case letters are=",upper_case)


# In[122]:


#58. Take a char from the user and find out how many number of occurrences are there in given string

a=input("Enter any string: ")
b=input("Enter any char to find out how many number of occurances are there in given string: ")
for i in a:
    c=a.count(b)
print("{} occured {} times".format(b,c))


# In[129]:


# 59. Take a element from the user and find out how many times the element occurred in given list
a=list('abcdabdcaadbdb')
print(a)
b=input("Enter any element to find out how many times the element occurred in the given list=")
count=0
for i in a:
    if i==b:
        count +=1
print("{} occured {} times".format(b,count))


# In[128]:


#60. Take an element from the user and find out how many number of occurrences are there in given tuple
a=tuple('abcdabdcaadbdb')
b=input("Enter any element to find out how many number of occurrences are there in a given tuple=")
count=0
for i in a:
    if i==b:
        count +=1
print("{} occured {} times".format(b,count))


# In[155]:


'''61. Reverse the string without effecting the special symbols. It involves three variations. Write
code for three variations.'''

s = 'ab!cd&'
op = ''
for i in s:
    if i.isalnum():
        op += i

op1 = op[::-1]
res = ''
print(s, len(s))
print(op1)
j = 0
for i in range(len(s)):
    if not s[i].isalnum():
        print(i, 'inside if', s[i])
        res += s[i]
    else:
        if j < len(op1):
            print(op1[j], i, j)
            res += op1[j]
            j += 1

print(res)

        
        


# In[140]:


'''62.Input: abc123,#$45def6%$^789$%^, output: $%^987%$^6fed54,#$321cba'''


# In[ ]:


'''63.Input: abc123,#$45def6%$^789$%^, output: 9876fe,#$d54321%$^cba$%^'''


# In[2]:


'''64.Inout: "123,#$456%$^789$%^", Output: 321,#$654%$^987$%^
		Only numbers has to reverse.
 '''
s = "123,#$456%$^789$%^"
op = ''
tem = ''
for i in s:
    if i.isdigit():
        tem += i
    else:
        op += tem[::-1] + i
        tem = ''
print(op)


# In[164]:


'''65. define a function to take person details name and age are mandatory 
parameters and height weight are optional parameters. If the user willing to 
pass any other details(like adhar, cell, pan, passport etc..) regarding him then 
your function should access those details.'''

def func(name, age, height = None, weight = None, **kwargs):
    print(name, age)
    if height is not None:
        print(height)
    if weight is not None:
        print(weight)
    for i in kwargs.items():
        print(i)
func("John", 25, height=175, weight=70, adhar="1234567890", cell="9876543210")


# In[4]:


'''65a. rewrite above assignments by functions. Can use string functions to solve the string related assignments'''

def even(a):
    if a%2==0:
        print("The given value is a even number")
    else:
        print("The given value is not a even number")
n=int(input("Enter any number: "))
even(n)


# In[ ]:


# 65 c. write a function to check given value is prime or not
def prime(n):
    if n>1:
        for i in range(2,n//2):
            if n%i == 0:
                print("{} is not a prime number".format(n))
                break
        else:
            print("{} is a prime number".format(n))
    else:
        print("{} is not a prime number".format(n))
a=int(input("Enter any number: "))
prime(a)


# In[ ]:


# 65 d. write a function to check given 2 values are divisible or not
def check(a,b):
    if a%b == 0:
        print("The given two values are divisible")
    else:
        print("The given two values are not divisible")
x=int(input("Enter any number: "))
y=int(input("Enter any number: "))
check(x,y)


# In[ ]:


# 67. take a string from the user and check contains only digits or not?
a=input("Enter any string: ")
if a.isdigit():
    print("The given string contains only digits")
else:
    print("The given string does not contains only digits")


# In[ ]:


# 68. take a string from the user and check contains only alphabets or not?
a=input("Enter any string: ")
if all(a.isalpha() for i in a):
    print("The given string contains only alphabets")
else:
    print("The given string does not contain only alphabets")


# In[ ]:


# 69. take a string from the user and check contains only special chars or not?
a=input("Enter any string: ")
if all(not i.isalnum() for i in a):
    print("The given string contains only special characters")
else:
    print("The given string does not contain only special characters")


# In[ ]:


# 70. take a string from the user and check contains only capital letters or not?
a=input("Enter any string: ")
if a.isupper():
    print("The given string contains only upper case letters")
else:
    print("The given string does not contains only upper case letters")


# In[ ]:


# 71. take a string from the user and check contains only small letters or not?
a=input("Enter any string=")
if a.islower():
    print("The given string contains only small case letters")
else:
    print("The given string does not contain only small case letters")


# In[8]:


#72. WAP to replace last n occurrence.
s = 'abcabccbabaa'
n = input('enter a target character: ')
o = int(input('enter no. of occurences: '))
op = ''
c = s.count(n)
j = 0
for i in s:
    if i==n:
        j += 1
        
    if j>=c:    # incomplete
    


# In[ ]:


# 73. WAP to check given string contains numbers or not. it should consider float numbers also.

# s = eval(input("Enter input: "))
# if type(s)==int or type(s)==float:
#     print("String contains number")
# else:
#     print("String does not contains number")    

s = input("Enter input: ")
try:
    op = float(s) or int(s)
    print('The string contains numbers.')
except ValueError:
    print("The string does not contain numbers.")


# In[ ]:


# 74. Convert the total string in to lower case.
# Convert the total string in to upper case.
a=input("Enter any string=")
print("converting total string in to lower case=",a.lower())
print("converting total string in to upper case=",a.upper())


# In[15]:


# 75. Convert every word start letter into caps. Some how title not working if it contains numbers
# and special symbols in the word

s = 'happy new year h@@l s878kjf'
op = ''
for i in range(len(s)):
    if i==0 or s[i-1]==' ':
        op += s[i].upper()
    
    else:
        op += s[i]
print(op)
    



# In[ ]:


'''76.replace last two occurrences of given source string with destination string
 preserve the delimiter after split.'''



# In[20]:


'''77. write a program to check given substring is there in actual string or not? (search should be case insensitive)
example: act="python is a pure object oriented programing language" '''

act = "python is a pure object oriented programing language"
sub = input('enter a sub string to check: ')
if sub in act:
    print('yes')
else:
    print('no')


# In[21]:


#79. l=[10,20,30,[40,50,60],70,[80,90,20]]. Convert this list as single dimensional list

l=[10,20,30,[40,50,60],70,[80,90,20]]
op = []
for i in l:
    if type(i) == list:
        op.extend(i)
    else:
        op.append(i)
print(op)


# In[22]:


# 80. input: "Google" print count of each character
s = 'google'
for i in set(s):
    print(i, s.count(i))


# In[ ]:


# 81. Convert n dimensional list to single dimensional list.
l=[10,20,30,[40,50,60],70,[80,90,20]]
op = []
for i in l:
    if type(i) == list:
        op.extend(i)
    else:
        op.append(i)
print(op)


# In[28]:


#82. l=[1,2,3] just make it as a string.
s = ''
l=[1,2,3]
for i in l:
    s += str(i)
print(s)


# In[ ]:


# 83. l=[1,2,3,[4,5,6],7,[8,9,10]] for single dimensional list
a=[1,2,3,[4,5,6],7,[8,9,10]]
b=[]
for i in a:
    if type(i) != list:
        b.append(i)
    else:
        for j in i:
            b.append(j)
print(b)


# In[ ]:


# 84. l=['a','A','b','B','d','D','c','C'] WAP to find 
# out case insensitive count and 85. case insensitive search for an element.


# In[31]:


# 86. l=['a','A','b','B','d','D','c','C']  sort the list properly
l=['a','A','b','B','d','D','c','C']
print(sorted(l))


# In[36]:


# 87. find the start position of the largest block of repeated characters in a given string

s = 'happynewyeargooodmorningrepetedz'
for i in set(s):
    if s.count(i)>2:
        print(s.index(i), i)


# In[37]:


# 88. WAP to find union and intersection of lists.
s1 = {1, 2, 3}
s2 = {4, 2, 5, 1, 6}
print(s1.union(s2))
print(s1.intersection(s2))


# In[ ]:


89. input: fun(5) output: [1,2,3,4,3,2,1]
90. input fun('abc') output: [[],][a],[b],[c],[a,b],[b,c],[c,a],[a,b,c]]


# In[39]:


# 91. Remove duplicates from the list: a=[1,2,3,2,3,4,1,,3,4]
a=[1,2,3,2,3,4,1,3,4]
op = []
for i in a:
    if i not in op:
        op.append(i)
print(op)    


# In[ ]:


92. l=['1','2','3'] get the sum of the list
93. l1=[1,2,3,4] l2=[5,6,7,8] sum of two lists
94. Find third max value of element in a list with soring and without sorting a list.


# In[ ]:


# 95. Input = ["1/1","1/2","1/3","1/4","2/5","2/6","2/8"] Output = [['1/1-4'], ['2/5-6'], ['2/8']]


# In[43]:


# 96. l=[1,2,3,5,7,8,9,10,11,12,13,20,22,23,24,25,26,27,20,21,22,4] 
# output = [[1, 2, 3], [5], [7, 8, 9, 10, 11, 12, 13], [20], [22, 23, 24, 25, 26, 27], [20, 21, 22], [4]]

l = [1,2,3,5,7,8,9,10,11,12,13,20,22,23,24,25,26,27,20,21,22,4]
op = []
res = []
for i in range(len(l)-1):
    
    if l[i]+1 == l[i+1]:
        res.append(l[i])
    else:
        op.append(res)
        op.append(l[i])
        res = []
print(op)


# In[46]:


# 97. input = 1,2,3,4,5,6,8,10 output = odd,even,odd,even,odd,even,even,even
a=1,2,3,4,5,6,8,10
for i in a:
    if i%2==0:
        print("even",end=",")
    else:
        print("odd",end=",")


# In[ ]:


'''98. input n=3
    		output:     111
        		101
        		111 '''


# In[ ]:


# 99. input: Google
# output: {"g":2,"o":2,"l":1,"e":1} use dictionary comprehension

a="Google".lower()
d={}
for i in a:
    d[i]=a.count(i)
print(d)


# In[47]:


# 100. keys=['k1','k2'], values = ['v1','v2'] form a dictionary.
keys=['k1','k2']
values = ['v1','v2']
d = dict()
for i in range(2):
    d[keys[i]] = values[i]
print(d)


# In[2]:


'''101. Sort the list marks = [("mohan", 80), ("satish", 90), ("purnesh", 40), ("venkat", 30)] 
according to descending order of marks'''

marks = [("mohan", 80), ("satish", 90), ("purnesh", 40), ("venkat", 30)]

op = sorted(marks, key = lambda x:x[1], reverse = True)
print(op)
 
        
    


# In[8]:


'''102.write a function to get dynamic list for floating numbers also based on strat and end and step parameters'''

def func(s, e, st):
    l = []
    op = s
    
    while op<=e:
        l.append(op)
        op += st
    return l
s = int(input('enter start number: '))
e = int(input('enter end range: '))
st = float(input('enter step in floating point: '))
print(func(s, e, st))
    


# In[18]:


'''103. find out all perfect numbers in given range'''

def func(s, e):
    op = []
    for i in range(s, e+1):
        m = 1
        for j in range(2, s//2+1):
            if i%j==0:
                m += j
        if m==i:
            op.append(i)
    return op

print(func(1, 10))  #incomplete


# In[19]:


'''104. WAP to do all stack operations using lists'''

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            print("Stack is empty. Cannot pop.")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            print("Stack is empty. Cannot peek.")

    def size(self):
        return len(self.items)

stack = Stack()

stack.push(1)
stack.push(2)
stack.push(3)

print("Popped:", stack.pop())
print("Peeked:", stack.peek())
print("Is empty?", stack.is_empty())
print("Size:", stack.size())


# In[22]:


class Stack:
    def __init__(self):
        self.l = []
    
    
    def is_empty(self):
        return len(self.l) == 0
    
    def push(self, val):
        self.l.append(val)
        return l
    def pop(self):
        if not self.is_empty():
            return self.l.pop()
    def peek(self):
        if not self.is_empty():
            return self.l[-1]
        else:
            print('list is empty')
    def size(self):
        return len(l)
s = Stack
s.push(10)
s.push(20)


# In[ ]:


'''105.WAP to do all queue operations using lists

'''


# In[2]:


'''106. WAP to remove n occurrences of specified element from a list'''

l = ['a', 'b', 'a', 'c', 'a', 'b', 'a', 'a', 'c', 'b']
t = input('enter a specified element: ')
n = int(input('enter no. of occurrences: '))
c = 0
for i in l:
    if i == t:
        c += 1
    if c<=n:
        l.remove(i)
print(l)
        


# In[7]:


'''107. compare two lists ignore order. i.e return True l1=[1,2,3,4],l2=[4,2,3,1], fun(l1,l2)-> True'''

l1=[1,2,3,4]
l2=[4,2,3,1]
def func(l1, l2):
    return True if sorted(l1) == sorted(l2) else False
print(func(l1, l2))


# In[10]:


'''108. XOR operation in python.'''

print(100 ^ 42)


# In[11]:


'''109. how to remove all occurrences of the given element in a list'''
l = ['a', 'b', 'a', 'c', 'a', 'b', 'a', 'a', 'c', 'b']
t = input('enter a specified element: ')
n = int(input('enter no. of occurrences: '))
c = 0
for i in l:
    if i == t:
        c += 1
    if c<=n:
        l.remove(i)
print(l)


# In[ ]:


'''110. how to remove first n occurrences of the given element in a list'''
'''111. how to remove last n occurrences of the given element in a list
112. how to remove nth occurrences of the given element in a list'''


# In[ ]:


'''113. WAP to generate list of floats i.e: fun(0,1,0.1), [0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]'''

def func(a, b, s):
    l = []
    res = a
    while res < b:
        l.append(res)
        res += s
    return l
print(func(0, 1, 0.1))


# In[ ]:


114. WAP to remove all occurrences of given substring from actual string
115. WAP to remove first n occurrences of given substring from actual string
116. WAP to remove last n occurrences of given substring from actual string
 117. WAP to replace last n occurrences of given substring with destination string in actual string
118. WAP to sort the string.
119. take a coma separated numbers and find out max number.
120. Read a json file. Try to get the information from the file


# In[ ]:


'''114. WAP to remove all occurrences of given substring from actual string'''

s = 'abcabacacabaab'
t = 'ab'
n = 3
for i in range(len(s)+1):
    if s[i-1]+s[i] == t:
        s.remove(t)

print(s)


# In[ ]:


s = 'abcabacacabaab'
t = 'ab'
n = 3

for _ in range(n):
    i = 0
    while i < len(s):
        if s[i:i+len(t)] == t:
            # Remove the substring
            print(s, s[:i], s[i+len(t):], i, len(t))
            s = s[:i] + s[i+len(t):]
            print(s)
        else:
            i += 1



# In[32]:


s = 'abcabacacabaab'
t = 'ab'
n = 3
print(s)
for _ in range(n):
    i = 0
    while i < len(s):
        if s[i:i+2] == t:
            s = s[:i] + s[i+len(t):]
        else:
            i += 1

print(s)


# In[27]:


print('kf')


# In[ ]:


'''120. Read a json file. Try to get the information from the file'''
import json

with open('abc.json', 'w+r') as f:
    f.write('{"name":"siri", "adrs":"hyd"}')
    data = f.read()
    print(json.load(data))
print('kdjfh')  


# In[ ]:




