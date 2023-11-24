#!/usr/bin/env python
# coding: utf-8

# In[5]:


""" 1  Take the input from the user for(Total number of people, Number of seats for bus. Based on two inputs 

Decide how many number of buses required """

no_of_people = int(input())
no_of_busses = int(input())
filled_busses = no_of_people // no_of_busses 
if filled_busses == 0:
    print(filled_busses)
else:
    print(filled_busses + 1)


# In[12]:


#2.take temperature from the user and convert foreign heat -> Celsius.
F = float(input("Enter Temperature in foreign heat "))
C = (F - 32) * 5/9
print(C,"C")


# In[14]:


#3.take temperature from the user and convert Celsius → foreign heat. 
C = float(input("Enter Celsius "))
F = (1.8 * C) + 32
print(F,"F")


# In[17]:


'''4.take four number from the user (variables name it as x1,x2,x3,x4) 
  Do the below operations -- (x1+x2)**2, (x3+x4)**3 ,  variance standard deviation: sqrt(variance):  
  User math module. Math.sqrt(variance) 
  Regression y=mx+b ,  m=1.23,  b=0.045  ,find out y ,  y=m*(x1+x2+x3+x4)+b 
  Find the average of four numbers ,Find the sum of four numbers '''
from statistics import variance,mean
import math
x1  = int(input())
x2  = int(input())
x3  = int(input())
x4  = int(input())
m=1.23 
b=0.045 
y = m * (x1 +x2  +x3  +x4 ) + b
var = variance([x1,x2,x3,x4])
print((x1+x2)**2)
print((x3+x4)**3)
print("Variance -- ",var)
print("Standard_Deviation --" , math.sqrt(var))
print(y)
print(mean([x1,x2,x3,x4]))
print(sum([x1,x2,x3,x4]))


# In[ ]:


'''5.Take the distance in km  Show that in cm, meters, in milli meters, cents, feets, yards'''

distance_km = float(input())
print(f"The {distance_km}KM to CM is {distance_km*100000}CM")
print(f"The {distance_km}KM to M is {distance_km*1000}M")
print(f"The {distance_km}KM to MM is {distance_km*1000000}MM")
print(f"The {distance_km}KM to Cents is {distance_km*39370.1}")
print(f"The {distance_km}KM to Feets is {distance_km*3280.84}")
print(f"The {distance_km}KM to Yards is {distance_km*1093.61}")


# In[ ]:


#6.Take the size of your hard disk in GB  Show that in MB, KB, TB, PB 

disk_size = float(input("Enter size in GB:- "))
print(f'The size in {disk_size}GB to MB is {disk_size*1000}MB')
print(f'The size in {disk_size}GB to KB is {disk_size*1000000}MB')
print(f'The size in {disk_size}GB to TB is {disk_size*0.001}TB')
print(f'The size in {disk_size}GB to PB is {disk_size/1000000}PB')


# In[ ]:


'''7.  Take name, age, height from the user and print like below 

The details of the person: Name:name of the person, Age:age of the person, Height:height of the person 

Note: make sure that no space between : and a value and should be space after “COMA” '''

name = input()
age= input()
height=input()
print(f'The details of the person: Name:{name}, age:{age}, height:{height}')


# In[ ]:


#8. BMI calculation: take required parameters for BMI calculation from the user and calculate BMI of the person.
weight = float(input("Enter your weight"))
height=float(input("Enter your height"))
bmi = weight / (height*height)
print(round(bmi,2))


# In[21]:


'''9. name="Jayaram", age=1.6, height=3.5356234 ,weight=10.343856783 
      By using above inputs print the output Name:Jayaram, Age:1.6, Height:3.54, Weight:10.344 
      Note: Use format specifiers(%s, %d, %f) '''
name = "Jayaram"
age =  1.6
height = 3.5356234
weight = 10.343856783
print(f'Name:%s, Age:%.1f , Height:%.2f, Weight:%.3f'%(name,age,height,weight))


# In[1]:


#10. Take three upper case letters from the user convert in to small case. 
a = input()
print(a.lower())


# In[3]:


'''11. take base and exponent value from the user and print like in mathematics: 

  example: base=2, exponent=3: 23 

Use: 2\u00b3 '''


print(f'2\u00b3')


# In[ ]:


#12. Take some groceries cost prices and print total cost and average cost, what is the max cost, what is the minimum cost.

soap = int(input())
brush = int(input())
oil = int(input())
flour= int(input())
total = soap+brush+oil+flour
print(total)
print(total/4)
print(max(soap,brush,oil, flour))
print(min(soap,brush,oil,flour))


# In[5]:


'''13. Assign “ten” value to variable it is 10 otherwise assign “Not ten” 

       Note: write two versions of program 

Version1: use and operator 

Version2: use or operator  '''

i = int(input("Enter a value: "))
if 10 and i == 10:
    print("Ten")
else:
    print("Not Ten")
if 10 or i == 10:
    print("Ten")
else:
    print("Not Ten")


# In[ ]:


'''13. Take the input from the user for(Total number of people, total number of buses, Number of seats for bus, adjust factor).
 Based on four inputs Decide whether there is sufficient buses or not and give solution for how many extra buses required. '''


# In[ ]:


#14.Take number from the user decide whether it is even or odd. 

number = int(input())
check_even_or_odd = "even" if number%2==0 else "odd"
print(check_even_or_odd)


# In[ ]:


#15.take number from the user decide whether it is positive number or negative number

number = int(input())
positive_or_negative = lambda a : "positive" if a>0 else "negative"
print(positive_or_negative(number))


# In[ ]:


'''16.take a string from the user print the length. if the user not given anything then show an error message '''

s = input()
s_length = lambda s : len(s) if len(s)>0 else "error"
print(s_length(s))


# In[ ]:


'''17.code to perform mathematical operations. take two numbers from the user and show the below menu 

1. add, 2. sub, 3. mul, 4.div,  5.quit 

Enter an option: 

based on the option need to perform an operations '''

def math_operations(n1,n2,op):
    if op =="add":
        return n1+n2
    elif op=="sub":
        return n1-n2
    elif op=="mul":
        return n1*n2
    elif op =="div":
        return n1/n2
    else:
        return "done"
n1=int(input("Enter number 1: "))
n2 = int(input("Enter number 2: "))
print("1.add\n2.sub\n3.mul\n4.div\5quit")
op = input("Enter an option: ")
print(math_operations(n1,n2,op))


# In[ ]:


'''18. show the menu: 

   1. kids, 2. Men's ,3. Women's 

   Show the corresponding message based on the selection. 

   Option:1: you are a kid ,2: you are a gentlemen , 3: you are a good women 
   Mention error message if the option value >3. '''

def math_operations(op):
    if op == 1:
        return "You are a kid"
    elif op==2:
        return "You are a gentlemen"
    elif op==3:
        return "You are a good women"
 
    else:
        return "error"

op = int(input("1:kids \n 2:Men's \n 3:Women's \n Enter an option: "))
print(math_operations(op))


# In[1]:


'''19. write a program to chcek given substring is there in actual string or not? 

example: act="python is a pure object oriented programing language" 

check whether “pure” is there in act or not. 

Note: Use in operator'''

org = input("Enter original string: ")
sub = input("Enter substring: ")
print(sub in org)


# In[3]:


#20. Take three numbers from the user and decide which is big 
n1,n2,n3 = list(map(int,input().split(" ")))
print("Big number out of three: ", max(n1,n2,n3))


# In[4]:


'''21. Take age and gender from the user and decide whether he is eligible for 	marriage in India or not. 

Age criteria: men age>24, women>21 '''

def eligibility_check(age,gender):
    if age >21 and gender =="women":
        return "Eligible for marriage in India"
    elif age >24 and gender =="men":
        return "Eligible for marriage in India"
    else:
        return "Not Eligible "
age = int(input("Enter your age: "))
gender = input("Enter your gender: ")
print(eligibility_check(age, gender))


# In[6]:


'''22. Take an age  and gender from the user: and mention that what he/she can 	do in india. 

""" 

conditions 

      1. Theatre: 5 for men 7 for women 
      2. Voting system: 18 for men and women 
      3. Marriage in india: 23 for men and for women >21 
      4. For govt jobs: (min:18, max:32)  for men and (min:18, max:34) for 	women 
      5. For driving licence: (min:18, max:60) for men and women 
 Eligibility: 
    
    1. theatre, 2.  Voting system , 3.  Marriage in india ,4.  For govt obs , 5. For driving licence: 

 Enter an option: 

Gender: 

    1. men   2. women 

Enter an option: 

Enter an age of person: '''

def eligibility_in_india(gender,age):
    if (age>=21) and gender =="women":
        print("You are eligible for marriage")
    if (age>=24) and gender =="men":
        print("You are eligible for marriage")
    if (age>=18 and age<=60) and (gender =="men" or "women"):
        print("You are Eligible for Driving licence")
    if (age>=18) and (gender =="men" or "women"):
        print("You are  Eligible for Voting System")
    if (age>=18 and age<=34) and gender =="women":
        print("You are eligible for Govt jobs \n  ")
    if (age>=18 and age<=32) and gender =="men":
        print("You are  Eligible for Govt jobs \n ") 
    if (age >5 and gender== "men") or (age>7 and gender=="women"):
        print("You are Eligible for Theatre ")
age =int(input("Enter your Age: "))
gender=input("Gender: \n 1.men \n 2. women \n Enter your gender: ")
eligibility_in_india(gender,age)


# In[7]:


'''23. operating systems: 

   1.windows , 2.android , 3.mac 

   Enter an option: 

   If the user enters 1 then show "Goto first floor and buy windows laptop or mobile" 

   If the user enters 2 then show "Goto second floor and buy adroid mobiles" 

   If the user enters 3 then show "Goto third floor and buy mac laptop or iphones" 

   If the user enters other than 1 or 2 or 3 then show "There is only three floors, please select 1 or 2 or 3" '''

def system_operating(op):
    if op == 1:
        return "Goto first floor and buy windows laptop or mobile"
    elif op==2:
        return "Goto second floor and buy adroid mobiles" 
    elif op==3:
        return "Goto third floor and buy mac laptop or iphones" 
 
    else:
        return "There is only three floors, please select 1 or 2 or 3"

op = int(input("Operating Systems \n 1:windows\n 2:android\n 3:mac\n Enter an option: "))
print(system_operating(op))


# In[8]:


#24.Given an age, figure out whether someone's a baby, toddler, child, teenager, adult or old codger. 

def check_category(age):
    if age <= 2:
        print("This person is a baby")
    elif 3 <= age <= 4:
        print("This person is a toddler")
    elif 5 <= age <= 12:
        print("This person is a child")
    elif 13 <= age <= 19:
        print("This person is a teenager")
    elif 20 <= age <= 64:
        print("This person is an adult")
    else:
        print("This person is an old codger")
age = int(input("Enter your age: "))
check_category(age)


# In[ ]:


#25.Take two number a,b from the user and check whether a is divisible by b or not 

a,b = input().split()
print(int(a)%int(b)==0)


# In[10]:


#26take a number from the user and check whether it is prime? 
def check_isPrime(number):
    count = 0 
    for i in range(2,number):
        if number % i == 0:
            count += 1 
    if count==0:
        print("Given number is prime Number")
    else:
        print("Given number is not a prime number")
number = int(input("Enter any number"))
check_isPrime(number)


# In[11]:


#26. take a string from the user and check contains only digits or not? 
s = input()
print(s.isdigit())


# In[12]:


#27. take a string from the user and check contains only  alphabets or not? 
print(input("Enter string: ").isalpha())


# In[16]:


#28. take a string from the user and check contains only  special chars or not? 
s = input()
print(s.isalnum())


# In[17]:


#29.take a string from the user and check contains only  capital letters or not? 
print(input("Enter string: ").isupper())


# In[ ]:


#30.take a string from the user and check contains only  small letters or not? 
print(input("Enter string: ").islower())


# In[ ]:


'''31. WAP to replace last n occurrence of give string. 

For example:”apple,orange,apple,grape,orange,apple,apple,orange” 

source: “apple” 

last occurrences: 2 

replace with: APPLE 

output:”apple,orange,apple,grape,orange,APPLE,APPLE,orange” '''

s = "apple,orange,apple,grape,orange,apple,apple,orange"
list_s = s.split(",")
new = list_s[::-1]
c = 0
for i in range (len(list_s[::-1])):
    if new[i] == 'apple':
        new[i] = "APPLE"
        c += 1
        if c == 2:
            break       
        
print(",".join(new[::-1]))  


# In[4]:


'''32. WAP to check given string contains numbers or not. it should consider float numbers also.'''
def contains_number_or_not(string):
    count = 0
    for i in string:
        if i.isdigit() or i==".":
            count += 1 
    if count == len(string):
        print("String contains numbers")
    else:
        print("String does not contains numbers")
string = input("Enter string: ")
contains_number_or_not(string)


# In[ ]:


#33. Convert the total string in to lower case. Without using lower() function. 
print(input("Enter string: ").swapcase())


# In[ ]:


#34. Convert the total string in to upper case. Without using upper() function. 
print(input("Enter string: ").swapcase())


# In[2]:


'''35. Show the below menu to the user until and until user select quit and display corresponding os message 

   Menu: 1. windows ,2. Linux , 3. Mac ,4. quit ''' 

while True:
    print("\tMenu: \n 1.windows\n 2.Linux\n 3.Mac\n 4.quit")
    op = input("Enter any operating System: ")
    if op in ["windows","Linux","Mac"]:
        pass
    else:
        break


# In[13]:


#36. take a string from the user and check contains at least one digit or not? 
import re
string = input("Enter string: ")
string_contains_digit = lambda string: True if re.search(r'[0-9]+',string) else False
print(string_contains_digit(string))


# In[14]:


#37. take a string from the user and check contains at least one alphabets or not? 
import re
string = input("Enter string: ")
string_contains_alpha = lambda string: True if re.search(r'[a-zA-Z]+',string) else False
print(string_contains_alpha(string))


# In[2]:


#38. take a string from the user and check contains at least one chars or not? 

string = input("Enter input:- ")

if len(string)>=1:
    print("String contains at least one chars")
else: 
    print("String does not contains at least one chars")


# In[15]:


#39. take a string from the user and check contains at least one capital letter or not?
import re
string = input("Enter string: ")
string_contains_alpha = lambda string: True if re.search(r'[A-Z]+',string) else False
print(string_contains_alpha(string))


# In[16]:


#40. take a string from the user and check contains at least one small letter or not? 
import re
string = input("Enter string: ")
string_contains_alpha = lambda string: True if re.search(r'[a-z]+',string) else False
print(string_contains_alpha(string))


# In[ ]:


#41. Print the first 100 odd numbers 

count = 0
number = 1 
while True:
    if count == 100:
        break 
    if number %2 == 1:
        print(number,end=",")
        count += 1 
    number += 1


# In[3]:


#42. Determine the factors of a number entered  by the user 

number = int(input())
factors_of_n = [i for i in range(1, number+1) if number%i ==0]
print(factors_of_n)


# In[2]:


'''43. Play a number guessing game (User enters a guess, you print YES or Higher or Lower). This should continue until and 
until user gives a correct number or want to quit in the middle.Get a hidden number by using random.randint(1,100) ''' 

import random
while True:
    print("Enter any number 1 to 100")
    user_input = input()
    random_number = random.randint(1,100)
    if user_input == 'q':
        break
    elif int(user_input) == random_number:
        print("YES, Your answer correct")
    elif int(user_input) < random_number:
        print("Lesser number")
    elif int(user_input) > random_number:
        print("Larger number")
    c = input("If you want to continue :\n 1.Y\n 2.No:  ")
    if c == "No":
        break
    else:
        continue
    


# In[ ]:


#44. Take two numbers from the user a,b check whether a is divisible by b or not? 

a,b = input().split(",")
print(int(a)%int(b)==0)


# In[ ]:


#45. Find the sum of all the multiples of 3 or 5 below 1000 

def sum_multiple_3_or_5():
    total= 0 
    for i in range(1,1000):
        if i%3==0 or i%5==0:
            total += i 
    return total 
print(sum_multiple_3_or_5())


# In[ ]:


#46. Write a program to find out big of two numbers 
big = lambda a,b : a if a>b else b
print(big(10,20))


# In[ ]:


#47. Write a program to find out biggest number in the given numbers. 
numbers = list(map(int,input().split()))
print(max(numbers))


# In[ ]:


#48. find out the index of  third occurrence of given substring 
string = input()
sub_string = input()
index = -1
for i in range(3):
    index = string.find(sub_string,index+1)
print(index)


# In[12]:


#49. find out the index nth occurrence of given substring 
original_string = input("Enter string: ")
substring = input("Enter substring: ")
nth_index = original_string[::-1].find(substring)
print(len(original_string)-nth_index)


# In[4]:


#50. Take some single digit numbers from the user and findout min, maximum, sum, average
single_digit_numbers = list(map(int,input("Enter any single digit numbers: ").split()))
print("Minimum of all numbers ",min(single_digit_numbers))
print("Maximum of all numbers ",max(single_digit_numbers))
print("Sum of all numbers ",sum(single_digit_numbers))
print("Average of all numbers ",sum(single_digit_numbers)/len(single_digit_numbers))


# In[14]:


'''51. print the number in proper mathematical way. 

Consider that we have 6 digit numbers. 

Number format  WAP> 10 -> 000010 , 100 ->  000100 , 1000 ->  001000 , 2345678  ->  2345678 

If the number has more than 6 digits then print as it is. '''

number = input("Enter number: ")
if len(number) >6:
    print(number)
else:
    print("%06d" % int(number))


# In[17]:


#52. names  ="emp1,emp2,emp3,emp4" iterate through the employee names. 
names = input("Enter names: ").split(",")
for name in names:
    print(name)


# In[ ]:


'''53. Take actual string, source string, destination string. 
replce first nth occurrences of source string with destination string of actual string. '''

actual_string = input()

source_string = input()
dest_string = input()

row = actual_string[::-1].replace(source_string[::-1], dest_string[::-1],1)
print(row[::-1])


# In[ ]:


'''54. Take a two numbers from the user and do below menu driven operations 

1. addition, 2. multiples, 3.division , 4.sqrt, 5. pow  a**b , 6.subtraction   

After selection do the corresponding operation. 

Note: user may give int, or float numbers. You should check whether it is proper digits or not. 
I.e the user given string should be in the position to convert to float. Other wise show the “inproper string given” Error.'''
import math
num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
if (type(num1)== int or float) and (type(num2) == int or float) :
    op = int(input("Enter option:\n 1.addition\n 2.subtraction\n 3.multiplication\n 4.division\n 5.sqrt\n 6.pow"))
    if op == 1:
        a = int(num1) + int(num2)
        print("Addition of two numbers: ",a)
    elif op == 2:
        s = num1 - num2
        print("Subtraction of two numbers: ",s)
    elif op==3:
        m = num1 * num2
        print("Multiplication of two numbers: ",m)
    elif op == 4:
        d = num1 / num2
        print("Division of two numbers: ",d)
    elif op==5:
        sqt = math.sqrt(num1,num2)
        print("Sqrt of two numbers: ",sqrt)
    elif op==6:
        p = num1 ** num2
        print("power of two numbers: ", p)
else:
    print("Given improper string")


# In[ ]:


#55. Take numbers from the user and find out min, maximum, sum, average 

numbers = list(map(int,input("Enter any numbers: ").split()))
print("Minimum of all numbers ",min(numbers))
print("Maximum of all numbers ",max(numbers))
print("Sum of all numbers ",sum(numbers))
print("Average of all numbers ",sum(numbers)/len(numbers))


# In[6]:


'''56. l=[1,2,3,5,7,8,9,10,11,12,13,20,22,23,24,25,26,27,20,21,22,4] find out how many even numbers are there and how many odd
numbers are there and how many positive numbers are there and how many negative numbers are there and how many prime numbers 
are there and how many perfect numbers are there and how many Armstrong numbers are there and how many palindrome numbers 
are there. '''


l = list(map(int,input().split()))
even_numbers = [i for i in l if i%2==0 ]
odd_numbers = [i for i in l if i%2==1]
positive_numbers = [i for i in l if i>0]
negative_numbers = [i for i in l if i<0]
def check_prime_numbers(l):
    prime_count = 0
    for i in l:
        count = 0 
        for j in range(2,i):
            if i%j == 0 :
                count += 1
        if count == 0 :
            prime_count += 1
    return prime_count
def count_perfect_numbers(l):
    perfect_number_count = 0
    for i in l:
        sum_prime = 0
        count = 0
        for j in range(2,i):
            if i%j ==0:
                count += 1
        if count == 0:
            sum_prime += 1
        if sum_prime == i:
            perfect_number_count +=1
    return perfect_number_count
        
print(len(even_numbers))
print(len(odd_numbers))
print(len(positive_numbers))
print(len(negative_numbers))
print(check_prime_numbers(l))
print(count_perfect_numbers(l))


# In[ ]:


57. Take a string from the user and find out how many digits are there, how many special symbols are there, how many small
letters are there, how many caps are there.


def string_count(string):
    digit_count = 0
    special_symbol_count =0
    small_letter_count =0
    caps_letter_count = 0 
    for i in string:
        if i.isdigit():
            digit_count +=1 
        elif i.islower():
            small_letter_count+=1 
        elif i.isupper():
            caps_letter_count +=1 
        else:
            special_symbol_count +=1 
    print(digit_count,small_letter_count,caps_letter_count,special_symbol_count)
string_count(input())


# In[1]:


#58. Take a char from the user and find out how many number of occurrences are there in given string 

string = input("Enter string")
char  = input("Enter char")
print("char count: ",string.count(char))


# In[ ]:


#59. Take a element from the user and find out how many times the  element occurred in given list 

lst =input().split()
ele = input()
ele_cnt = [ele for i in lst if i==ele]
print(len(ele_cnt))


# In[ ]:


#60. Take an element from the user and find out how many number of occurrences are there in given tuple 
tpl = ('t','g','r',4,'h','r',6,7,'h','t')
ele = input()
cnt =0
for i in tpl:
    if i==ele:
        cnt += 1 
print(cnt)


# In[16]:


'''61. Reverse the string.> without effecting the special symbols. It involves three variations. Write code for three variations. 
62.Input: abc123,#$45def6%$^789$%^, output: $%^987%$^6fed54,#$321cba '''
    
s = "abc123,#$45def6%$^789$%^"
sp_ch = ''
res = ''
num = [i for i in s if i.isalnum()]
for i in s[::-1]:
    if not i.isalnum():
        sp_ch = i + sp_ch
    else:
        if len(sp_ch) >0:
            res += sp_ch
            sp_ch = ''
        res += num[-1]
        num.pop(-1)
print(res)


# In[13]:


#63.Input: abc123,#$45def6%$^789$%^, output: 9876fe,#$d54321%$^cba$%^ 
s = "abc123,#$45def6%$^789$%^"
res = ''
num = [i for i in s if i.isalnum()]
for i in s:
    if i.isalnum():
        res  += num[-1]
        num.pop(-1)
    else:
        res += i 
print(res)
        


# In[10]:


# 64.Inout: "123,#$456%$^789$%^", Output: 321,#$654%$^987$%^ Only numbers has to reverse. 
s = "123,#$456%$^789$%^"
num = ''
result = ''
for i in s:
    if i.isdigit():
        num += i
    else:
        if len(num)>0:
            result = result + num[::-1]
            num = ''
        result += i 
print(result)


# In[ ]:


'''FUNCTIONS: 

65. define a function to take person details name and age are mandatory parameters and height weight are optional parameters. 
If the user willing to pass any other details(like adhar, cell, pan, passport etc..) 
regarding him then your function should access those details. '''

def user_details(name,age,height=0,weight=0,*args):
    print(name,age,height,weight,args)

user_details("john",20)


# In[ ]:


#65a. rewrite above assignments by functions. Can use string functions to solve the string related assignments 



# In[ ]:


#65 b. write a function to check given value is even or not 

def check_num(n):
    
    if n%2 == 0:
        return "Even"
    
    else:
        return "Odd"

n = int(input("Enter a number:- "))
num = check_num(n)
print(num)


# In[ ]:


#65 c. write a function to check given value is prime or not 

def check_prime(n):
    c = 0
    for i in range(1,n+1):
        if n%i == 0:
            c += 1
    if c == 2:
        return "It's Prime"
    else:
        return "Not Prime"

n = int(input("Enter a number:- "))
num = check_prime(n)
print(num)


# In[ ]:


#65 d. write a function to check given 2 values are  divisible or not 



# In[ ]:


#67. take a string from the user and check contains only digits or not? 

user = input("Enter input:- ")
if user.isdigit():
    print("The string contains only digits.")
else:
    print("The string does not contain only digits.")


# In[ ]:


#68. take a string from the user and check contains only  alphabets or not? 

user = input("Enter input:- ")

if user.isalpha():
    print("The string contains only alphabets.")
else:
    print("The string does not contain only alphabets")


# In[ ]:


#69. take a string from the user and check contains only  special chars or not? 

user = input("Enter input:- ")
if all(not i.isalnum() for i in user):
    print("The string contain only special characters")
else:
    print("The string does not contain special characters")


# In[ ]:


#70. take a string from the user and check contains only  capital letters or not? 

user = input("Enter input:- ")
if all(i.isupper() for i in user):
    print("The string contain only capital letters")
else:
    print("The string does not contain only capital letters")


# In[ ]:


#71. take a string from the user and check contains only  small letters or not? 
user = input("Enter input:- ")
if all(i.islower() for i in user):
    print("The string contain only lower letters")
else:
    print("The string does not contain only lower letters")


# In[ ]:


#72. WAP to replace last n occurrence. 
actual_string = input()

source_string = input()
dest_string = input()

row = actual_string[::-1].replace(source_string[::-1], dest_string[::-1],1)
print(row[::-1])


# In[ ]:


#73. WAP to check given string contains numbers or not. it should consider float numbers also. 


# In[ ]:


#74. Convert the total string in to lower case. Convert the total string in to upper case.
user = input("Enter input:- ")

print(user.lower())
print(user.upper())


# In[ ]:


#75.Convert every word start letter into caps.Some how title not working if it contains numbers and special symbols in the word

user = input("Enter a words space separated:- ").split()

if all(i.isalpha() for i in user):
    res = ""
    for i in user:
        res += i.title()+" "
    print(res)

else:
    print("Title not working if it contains numbers and special symbols in the word")


# In[ ]:


#76.replace last two occurrences of given source string with destination string preserve the delimiter after split. 

actual_string = input("Enter actual string:- ")

source_string = input("Enter source string:- ")
dest_string = input("Enter destination string:- ")

row = actual_string[::-1].replace(source_string[::-1], dest_string[::-1],2)
print(row[::-1])


# In[ ]:


#77. write a program to check given substring is there in actual string or not? (search should be case insensitive) 

example: act="python is a pure object oriented programing language" 

s = input()
sub_s = input()
s = s.lower()
print(sub_s in s)


# In[ ]:


#78.check whether “pure” is there in act or not. Note: Use in operator 
act = input("Enter input: ")
c = 'pure'
if c in act:
    print('The substring in there in actual string')
else:
    print("The substring is not there in actual string")


# In[ ]:


# 79. l=[10,20,30,[40,50,60],70,[80,90,20]]. Convert this list as single dimensional list 

l= [10,20,30,[40,50,60],70,[80,90,20]]
new_l = []
for i in l:
    if type(i) == int:
        new_l.append(i)
    else:
        for j in i:
            new_l.append(j)
print(new_l)


# In[2]:


#80. input: "Google" print count of each character

s = "Google"
for i in s:
    print(i,s.count(i))


# In[ ]:


#81. Convert n dimensional list to single dimensional list. 

l =[[1,3,2,"g"],[6,5,4],['v',8,9]]
new_lst =[]
for i in l:
    for j in i:
        new_lst.append(j)
print(new_lst)


# In[ ]:


#82. l=[1,2,3] just make it as a string. 

l = list(map(int,input().split()))
s =""
for i in l:
    s += i 
print(s)


# In[ ]:


#83. l=[1,2,3,[4,5,6],7,[8,9,10]] for single dimensional list 

l = [1,2,3,[4,5,6],7,[8,9,10]]
res = []
[res.extend(i) for i in a]
print(res)


# In[ ]:


#84. l=['a','A','b','B','d','D','c','C'] WAP to find out case insensitive count 

l=['a','A','b','B','d','D','c','C'] 
user = input("Enter input from list:- ")
c = 0
for i in l:
    if i.lower() == user.lower():
        c += 1
print("Count=",c)


# In[ ]:


#85. case insensitive search for an element.

user = input("Enter input from list:- ")
for i in l:
    if user.lower() in l:
        print("Have search element in list ")
        break


# In[ ]:


# 86. l=['a','A','b','B','d','D','c','C']  sort the list properly 

l=["a",'A','b','B','d','D','c','C']
print(sorted(l))


# In[25]:


#87. find the start position of the largest block of repeated characters in a given string 

def find_starting_position(s):
    length_l  = len(s)
    cur_count = 0 
    max_count = 0 
    req_pos = 0
    for i in range(length_l-1):
        if s[i] == s[i+1]:
            cur_count += 1
        else:
            if cur_count > max_count :
                max_count = cur_count
                req_pos = i - max_count
            cur_count =  0
    if cur_count > max_count:
        max_count = cur_count
        req_pos = length_l - max_count 
        
    return req_pos
s = input("Enter string:  ")
print(find_starting_position(s))
                                                                                                                                                                            


# In[ ]:


#88. WAP to find union and intersection of lists. 
l1=input().split()
l2= input().split()

def union_opn(l1,l2):
    union = l1
    for i in l2:
        if i not in l1:
            union.append(i)
    return union
def intersect_opn(l1,l2):
    intersect = []
    for j in l1:
        if j in l2:
            intersect.append(j)
    return intersect
print(union_opn(l1,l2))
print(intersect_opn(l1,l2))


# In[ ]:


#89. input: fun(5) output: [1,2,3,4,3,2,1] 

def fun(a):
    
    res = []
    for i in range(1,a):
        res.append(i)
    
    for i in range(1,a-1):
        res.append((a-1)-i)
        
    return res
print(fun(5)) 


# In[ ]:


#90. input fun('abc') output: [[],][a],[b],[c],[a,b],[b,c],[c,a],[a,b,c]] 

def fun(a):
    l = len(a)
    res = []
    for i in range(l+1):
        row = combinations("abc",i)
        res.append(row)
    
    final = []
    for i in res:
        new = list(i)
        for j in new:
            final.append(list(j))
            
    print(final)
        
fun('abc')


# In[ ]:


#91. Remove duplicates from the list: a=[1,2,3,2,3,4,1,,3,4] 
l=[1,2,3,2,3,4,1,3,4]
def remove_duplicates(l):
    without_duplicates=[]
    for i in l:
        if i not in without_duplicates:
            without_duplicates.append(i)
    return without_duplicates
print(remove_duplicates(l))


# In[ ]:


#92. l=['1','2','3'] get the sum of the list 
l=['1','2','3']
sum_l =0
for i in l:
    sum_l += int(i)
print(sum_l)


# In[ ]:


#93. l1=[1,2,3,4] l2=[5,6,7,8] sum of two lists 
l1=[1,2,3,4]
l2=[5,6,7,8]
res=[]
for i in range(len(l1)):
    res.append(l1[i]+l2[i])
print(res)


# In[ ]:


#94. Find third max value of element in a list with soring and without sorting a list. 

l = [10,23,43,12,34,56,66,25]
l.sort()
print("Third max value of element with sorting =",l[-3])

k = [10,23,43,12,34,56,66,25]
l = k[:]
for i in range(2):
    l.remove(max(l))
print("Third max value of element without sorting =",max(l))


# In[ ]:


#95. Input = ["1/1","1/2","1/3","1/4","2/5","2/6","2/8"] Output = [['1/1-4'], ['2/5-6'], ['2/8']] 



# In[ ]:


#96. l=[1,2,3,5,7,8,9,10,11,12,13,20,22,23,24,25,26,27,20,21,22,4] 
#output = [[1, 2, 3], [5], [7, 8, 9, 10, 11, 12, 13], [20], [22, 23, 24, 25, 26, 27], [20, 21, 22], [4]] 

l=[10,1,2,3,5,7,8,9,10,11,12,13,20,22,23,24,25,26,27,20,21,22,4] 

res = []
sub = []
for i in range(len(l)):
    if l[i] == l[i-1]+1:
        sub.append(l[i])
    
    else:
        res.append(sub)   
        sub = []
        sub.append(l[i])
res.append(sub)

print(res[1:])


# In[ ]:


#97. input = 1,2,3,4,5,6,8,10 output = odd,even,odd,even,odd,even,even,even 
inp =[1,2,3,4,5,6,8,10]
s=""
for i in inp:
    if i%2==0:
        s += "even,"
    else:
        s =s +"odd,"
print(s.strip(","))


# In[ ]:


'''98. input n=3 

    		output:     111 

        		101 

        		111 '''


# In[1]:


#99. input: Google output: {'g':2,'o':2,'l':1,'e':1} use dictionary comprehension 

ip = "Google".lower()

row = {i:ip.count(i) for i in set(ip)}
print(row)


# In[ ]:


#100. keys=['k1','k2'], values = ['v1','v2'] form a dictionary. 

keys=['k1','k2']
values = ['v1','v2']

row = {keys[i]:values[i] for i in range(len(keys))}
print(row)


# In[ ]:


#Sort the list marks = [("mohan", 80), ("satish", 90), ("purnesh", 40), ("venkat", 30)] according to descending order of marks 
    
list_marks = [("mohan", 80), ("satish", 90), ("purnesh", 40), ("venkat", 30)] 

row = sorted(list_marks, key=lambda x : x[1], reverse=True)
print(row)


# In[ ]:


#102.write a function to get dynamic list for floating numbers also based on strat and end and step parameters 

s = 1
e = 13.2
step = 1.2
res = []

while e > s:
    res.append(round(s,2))
    s += step
print(res)


# In[ ]:


#103. find out all perfect numbers in given range

def find_perfect(n):
    s = sum(filter(lambda x: n%x == 0, range(1,n)))
    return  s == n
         

start = 1
end = 100000
perfect = list(filter(lambda n : find_perfect(n), range(start, end+1)))
print(perfect)


# In[ ]:


#104. WAP to do all stack operations using lists 

class Stack:
    def __init__(self):
        self.items = []
    
    def push(self,item):
        self.items.append(item)
        print(f'Pushed in to stack of {item}')
    
    def empty(self):
        return len(self.items) == 0
    
    def pop(self):
        if not self.empty():
            p = self.items.pop()
            print(f"{p} Popped item from Stack")
    
    def display(self):
        if not self.empty():
            print("Stack=",self.items)
        else:
            print("Stack is empty")

obj = Stack()
obj.push(400)
obj.push(800)
obj.push(800)
obj.pop()
obj.display()


# In[ ]:


#105.WAP to do all queue operations using lists 

class Queue:
    def __init__(self):
        self.items = []
    
    def empthy(self):
        return len(self.items) == 0
    
    def enquee(self,item):
        self.items.append(item)
        print(f"{item} enqueed to the list")
    
    def dequee(self):
        if not self.empthy():
            pop_item = self.items.pop()
            print(f"{pop_item} dequeed from the list")
    
    def display_queue(self):
        print("Queue = ",self.items )

q = Queue()
q.enquee(200)
q.enquee(500)
q.enquee(200)
q.dequee()
q.display_queue()


# In[ ]:


#106. WAP to remove n occurrences of specified element from a list 

l = [1,2,34,2,3,4,5,6,7,8,9,2,4,6,8,9]
first = int(input("Enter element to remove:- "))
count = int(input("Enter occurrences:- "))
l = l[::-1]
for i in range(count):
    index = l.index(first)
    l[index] = -1
    l.pop(index)
print(l[::-1])


# In[ ]:


#107. compare two lists ignore order. i.e return True l1=[1,2,3,4],l2=[4,2,3,1], fun(l1,l2)-> True 

def fun(l1,l2):
    print(sorted(l1) == sorted(l2))

l1=[1,2,3,4]
l2=[4,2,3,1]
fun(l1,l2)


# In[ ]:


#108. XOR operation in python. 



# In[ ]:


#109. how to remove all occurrences of the given element in a list 


# In[ ]:


#110. how to remove first n occurrences of the given element in a list 

l = [1,2,34,2,3,4,5,6,7,8,9,2,4,6,8,9]
first = int(input("Enter element to remove:- "))
count = int(input("Enter occurrences:- "))

for i in range(count):
    index = l.index(first)
    l[index] = -1
    l.pop(index)
print(l)


# In[ ]:


#111. how to remove last n occurrences of the given element in a list 

l = [1,2,34,2,3,4,5,6,7,8,9,2,4,6,8,9]
first = int(input("Enter element to remove:- "))
count = int(input("Enter occurrences:- "))
l = l[::-1]
for i in range(count):
    index = l.index(first)
    l[index] = -1
    l.pop(index)
print(l[::-1])


# In[ ]:


#112. how to remove nth occurrences of the given element in a list 

l = [1,2,34,2,3,4,5,6,7,8,9,2,4,6,8,9]
n = int(input("Enter input:- "))
c = l.count(n)
copy = l[:]
last_index = 0
for i in range(c):
    index = copy.index(n)
    copy[index] = -1
    last_index = index
#print(last_index)
rm = l.pop(last_index)
print(f"{rm} removed last occurrences of specified element from a list")
print(l)


# In[ ]:


#113. WAP to generate list of floats i.e: fun(0,1,0.1), [0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9] 

def fun(a,b,c):
    res = []
    while b > a:
        res.append(round(a,2))
        a += c  
    print(res)
        
fun(0,1,0.1)


# In[ ]:


# 114. WAP to remove all occurrences of given substring from actual string 

actual_string = "apple orange apple mango grapes apple grapes apple banana"
substring = "apple"
print(actual_string.replace(substring,""))


# In[ ]:


#115. WAP to remove first n occurrences of given substring from actual string 

actual_string = "apple orange apple mango grapes apple grapes apple banana"
substring = "apple"
n = int(input("Enter number of occurrences:- "))
print(actual_string.replace(substring,"",n))


# In[3]:


#116. WAP to remove last n occurrences of given substring from actual string 
actual_string = "apple orange apple mango grapes apple grapes apple banana"
a = actual_string[::-1]
substring = "apple"
s = substring[::-1]

n = int(input("Enter number of occurrences:- "))
r = a.replace(s,'',n)
print(r[::-1])


# In[ ]:


#117. WAP to replace last n occurrences of given substring with destination string in actual string

actual_string = "apple orange apple mango grapes apple grapes apple banana"
substring = "apple"
dest_string = input("Enter destination string:- ")
n = int(input("Enter occurrences:- "))
a = actual_string[::-1]
s = substring[::-1]
d = dest_string[::-1]

res = a.replace(s,d,n)
print(res[::-1])


# In[ ]:


#118. WAP to sort the string. 

s = "apple"
print("".join(sorted(s)))


# In[ ]:


#119. take a coma separated numbers and find out max number. 

n = [12,34,45,67,43]
print(max(n))


# In[ ]:


#120. Read a json file. Try to get the information from the file 

import json

with open("person.json","r") as f:
    data = json.load(f)
print(data)


# In[ ]:


#121.Read a yaml file. Try to get the information from the file 

import yaml
#print(dir(yaml))
with open("yamal.yaml","r") as f:
    data = yaml.safe_load(f)
print(data)


# In[ ]:


#122.Read any image data using Opencv 


# In[ ]:


#123.make alternative words reversed in given string: ex: "python program good language"-> "python margorp good egaugnal" 

string = input().split(" ")
s =""
for i in range(len(string)):
    if i%2==1:
        s += (string[i][::-1]+" ")
        
    else :
        s+= (string[i]+" ")
    
print(s)


# In[ ]:


'''124. l=['c',"cpp","java","php","python"] 

 case insensitive count# l.count("C")->1 

like count l.own_count("c")->2 with case insensitive '''

l=['C',"cpp","java","php","python"]
res = "".join(l)
user1 = input("Enter charactor to count case sensitive:- ")
user2 = input("Enter charactor to count case insensitive:- ")

res1 = res.count(user1)
new = res.lower()
res2 = new.count(user2)

print("Count of case sensitive:-", res1)
print("Count of case insensitive:-", res2)


# In[ ]:


'''125: take total parameters, out of which few are optional and few are mandatory. Take some parameters from the user and 
    check whether the user given all the mandatory paramerters or not. 

For example: to insert person details 

Total parameters: name,age,height,pan,cell,adhar,passport 

mandatory: name,cell,adhar 

if the user given: name,adhar,passport then you need to print cell is mandatory parameter 

if the user given: name,cell,adhar,passport then you need to print ok  

if the user given: adhar,passport then you need to print cell,name are mandatory parameter '''
    

def total_parameters(**kargs):
    manadatory = ["name", "cell", "adhar"]
    parameters = ["name","age","height","pan","cell","adhar","passport"]
    #print(kargs)
    
    show_man = []
    
    for i in manadatory:
        if i not in kargs:
            show_man.append(i)
    
    #print(show_man)
    extra = []
    for j in kargs:
        if j not in parameters:
            extra.append(j)
    
    if len(show_man) == 0 and len(extra) == 0:
        return "ok"
    
    if len(show_man) != 0 and len(extra) == 0:
        return f"{show_man} manadatory items"
    
    if len(show_man) == 0 and len(extra) != 0:
        return f"{extra} extra items"
    
    if len(show_man) != 0 and len(extra) != 0:
        return f"{show_man} manadatory items and {extra} extra items"

print(total_parameters(adhar=6768433, passport=32333, weight=45))


# In[ ]:


'''126 Take two inputs from the user:  your program should check for below scenarios. 
10,20: 30 
12.34,45.67: 58.01 
+12,-12: 0 

qwe,23we: Enter digits or float values only '''
    
    
try:
    a,b = map(float, input("Enter values separated by comma:- ").split(","))
    print(sum([a,b]))
except ValueError as err:
    print(err,"please enter int or float values")


# In[ ]:


'''127. take the number of employees count from the user and ask the inputs required for the bmi for each and every person. The result should be like below 

empid:{“weight:”,”height”:,”age”:,”bmi”:0.9,”result”:”+ve”} '''
    
    
users = int(input("Enter the number of employees count:- "))
empid = 1000
for i in range(users):
    w = float(input("Enter weight(kgs):- "))
    h = float(input("Enter height(feets):- "))
    a = float(input("Enter age(years):- "))
    bmi = w/h
    result = ""
    if bmi < 25:
        result = "+ve"
    else:
        result = "-ve"
    
    print({empid:{"weight":w, "height":h, "age":a, "bmi":bmi, "result": result}})
    empid += 1


# In[ ]:




