#!/usr/bin/env python
# coding: utf-8

# # Assignments on variables expressions and statements

# In[56]:


##1.	Take the input from the user for(Total number of people,Number of seats for bus. Based on two inputs
##Decide how many number of buses required

no_of_people = int(input())
no_of_seats = int(input())
no_of_bus = no_of_people//no_of_seats
if no_of_people%no_of_seats != 0:
    no_of_bus += 1
print(no_of_bus)


# In[ ]:


##2.Take temperature from the user and convert foreign heat -> Celsius.
temp_f = float(input())
temp_c = (temp_f-32)*(5/9)
print(f'{temp_c}C')



# In[12]:


##3.Take temperature from the user and convert Celsius → foreign heat.
temp_c = float(input())
temp_f = temp_c*(9/5)+32
print(f'{temp_f}F')


# In[15]:


'''
4.Take four number from the user (variables name it as x1,x2,x3,x4)
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
x1,x2,x3,x4 = map(float,input().split())
res1 = (x1+x2)**2
res2 = (x3+x4)**3
mean = (x1+x2+x3+x4)/4
varience = ((x1-mean)**2 + (x2-mean)**2 + (x3-mean)**2 + (x4-mean)**2)/4
std_dev = math.sqrt(varience)
y = 1.23*(x1+x2+x3+x4)+0.045
avg = mean
sum_of_four = x1+x2+x3+x4
print(res1)
print(res2)
print(varience)
print(std_dev)
print(y)
print(avg)
print(sum_of_four)


# In[19]:


## 5.Take the distance in km
##  	Show that in cm, meters, in milli meters, cents, feets, yards
distance_km = float(input())
print(f"The {distance_km}KM to CM is {distance_km*100000}CM")
print(f"The {distance_km}KM to M is {distance_km*1000}M")
print(f"The {distance_km}KM to MM is {distance_km*1000000}MM")
print(f"The {distance_km}KM to Cents is {distance_km*39370.1}")
print(f"The {distance_km}KM to Feets is {distance_km*3280.84}")
print(f"The {distance_km}KM to Yards is {distance_km*1093.61}")


# In[22]:


## 6.Take the size of your hard disk in GB
##   	Show that in MB, KB, TB, PB
disk_size = float(input("Enter size in GB:- "))
print(f'The size in {disk_size}GB to MB is {disk_size*1000}MB')
print(f'The size in {disk_size}GB to KB is {disk_size*1000000}MB')
print(f'The size in {disk_size}GB to TB is {disk_size*0.001}TB')
print(f'The size in {disk_size}GB to PB is {disk_size/1000000}PB')



# In[25]:


'''
7. Take name, age, height from the user and print like below
The details of the person: Name:name of the person, Age:age of the person, Height:height of the person
Note: make sure that no space between : and a value and should be space after “COMA”
'''
name,age,height = map(str,input().split())
print(f'The details of the person: Name:{name}, age:{age}, height:{height}')


# In[27]:


##8. BMI calculation: take required parameters for BMI calculation from the user and calculate BMI of the person.
height = float(input("Enter your height:- "))
weight = float(input("Enter your weight:- "))
bmi = weight/(height**2) 
print("The BMI of yours is", bmi)


# In[1]:


'''
9.name="Jayaram"
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
info = "Name: %s, Age: %1f, Height: %2f, Weight: %3f"%(name, age, height, weight)
print(info)



# In[2]:


# 10. Take three upper case letters from the user convert in to small case.
letter = input("Enter Three Upper Case Letters:- ")
print(letter.lower())


# In[3]:


# 11.Take base and exponent value from the user and print like in mathematics:
# example: base=2, exponent=3: 23
base = input("Enter base value:- ")
exponent = input("Enter exponent value:- ")
ex = f'base={base}, exponent={exponent}: {base}^{exponent}'
print(ex)


# In[4]:


# 12. Take some groceries cost prices and print total cost and average cost, what is the max cost, what is the minimum cost.
cost_prices = [20,10,30,8,30,33,44,55,9,29]
total_cost = sum(cost_prices)
avg_cost = total_cost / len(cost_prices)
max_cost = max(cost_prices)
min_cost = min(cost_prices)
print("Total cost:-", total_cost)
print("Average cost:-", avg_cost)
print("Max cost:-", max_cost)


# # Variable Assignments:

# In[3]:


# 13. Assign “ten” value to variable it is 10 otherwise assign “Not ten”
# Note: write two versions of program
# Version1: use and operator
# Version2: use or operator

v = int(input())
if v == 0:
    print(v or 10)
else:
    print("not ten")
    


# In[5]:


v = int(input("Enter value:- "))

if v != 0:
    print(v and 10)
else:
    print("Not ten")


# # Conditional statements

# In[12]:


# 13. Take the input from the user for(Total number of people, total number of buses, Number of seats
#     for bus, adjust factor). Based on four inputs
#     Decide whether there is sufficient buses or not and give solution for how many extra buses required.

people = int(input("Enter number of people:- "))
buses = int(input("Enter number of buses:- "))
seats = int(input("Enter number of seats:- "))
factor = int(input("Enter adjust factor:- "))

#seats_per_bus = seats//buses
no_of_buses = (people)//(seats+factor)
print(no_of_buses)
if (people)%(seats+factor) != 0:
    no_of_buses += 1
    
    if buses > no_of_buses:
        print(f"{no_of_buses} buses required but")
        print(f"{buses-no_of_buses} extra buses are their")
    else:
        print("No Sufficient buses")
        print(f"{no_of_buses-buses} buses are required")
        
else:
    print("Sufficient buses")
    

    


# In[7]:


# 14.Take number from the user decide whether it is even or odd.

value = int(input("Enter a value:- "))
if value%2 == 0:
    print("EVEN")
else:
    print("ODD")


# In[10]:


# 15.take number from the user decide whether it is positive number or negative number

num = input()
if num[0] == "-":
    print("Negative number")
else:
    print("Positive number")


# In[14]:


# 16.take a string from the user print the length. if the user not given anything then show an error message

string = input("Enter a word:- ")
len_string = len(string)
print(len_string) if len_string else "Error"
    


# In[23]:


'''
17.Code to perform mathematical operations. take two numbers from the user and show the below menu
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


# In[28]:


'''
18. show the menu:
    1. kids
    2. Men's
    3. Women's
    Show the corresponding message based on the selection.
    Option:1: you are a kid
    2: you are a gentlemen
    3: you are a good women
    Mention error message if the option value >3.
'''

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


# In[29]:


'''
19. Write a program to chcek given substring is there in actual string or not?
    example: act="python is a pure object oriented programing language"
    heck whether “pure” is there in act or not.
    Note: Use in operator
'''

string = input("Enter a string:- ")
sub_string = input("Enter a sub-string:- ")

if sub_string in string:
    print("YES")
else:
    print("NO")


# In[37]:


# 20. Take three numbers from the user and decide which is big
v1,v2,v3 = map(int, input("Enter three values separated by space:- ").split())

big = 0

if v1 > v2 and v1 > v3:
    big = v1
elif v2 > v1 and v2 > v3:
    big = v2
else:
    big = v3
print(big)


# In[41]:
#comments


# 21. Take age and gender from the user and decide whether he is eligible for marriage in India or not.
# Age criteria: men age>24, women>21

user_age = int(input("Enter your age:- "))
gender = input("Enter your gender:- ")

if gender == "men":
    if user_age > 24 :
        print("Eligible for marriage in India")
    else:
        print("Not eligible for marriage in India")
elif gender == "women":
    if user_age > 21 :
        print("Eligible for marriage in India")
    else:
        print("Not eligible for marriage in India")
    
        
    


# In[3]:


'''
22. Take an age and gender from the user: and mention that what he/she can do in india.
    conditions
       1. Theatre: 5 for men 7 for women
       2. Voting system: 18 for men and women
       3. Marriage in india: 23 for men and for women >21
       4. For govt jobs: (min:18, max:32) for men and (min:18, max:34) for women
       5. For driving licence: (min:18, max:60) for men and women
    Eligibility:
       1. theatre
       2. Voting system
       3. Marriage in india
       4. For govt obs
       5. For driving licence:
    Enter an option:
       Gender:
       1. men
       2. women
    Enter an option:
    Enter an age of person:
'''

age = int(input("Enter your age:- "))
gender = input("Enter your gender:- ")

if gender == "men":
    if age >= 5:
        print("He can eligible for theatre in India")
    if age >= 18:
        print("He can eligible for voting system in India")
    if age >= 23:
        print("He can eligible for marriage in India")
    if age >= 18 and age <= 32:
        print("He can eligible for government jobs in India")
    if age >=18 and age <= 60:
        print("He can eligible for driving licence in India")
    if age < 5:
        print("Not eligible")
elif gender == "women":
    if age >= 7:
        print("He can eligible for theatre in India")
    if age >= 18:
        print("He can eligible for voting system in India")
    if age >= 21:
        print("He can eligible for marriage in India")
    if age >= 18 and age <= 34:
        print("He can eligible for government jobs in India")
    if age >=18 and age <= 60:
        print("He can eligible for driving licence in India")
    if age < 6:
        print("Not eligible")


# In[46]:


'''
23. Operating systems:
      1.windows
      2.android
      3.mac
    Enter an option:
      If the user enters 1 then show "Goto first floor and buy windows laptop or mobile"
      If the user enters 2 then show "Goto second floor and buy adroid mobiles"
      If the user enters 3 then show "Goto third floor and buy mac laptop or iphones"
      If the user enters other than 1 or 2 or 3 then show "There is only three floors, please select 1 or 2 or 3"
'''

user = int(input("Enter an option:- "))
if user == 1:
    print("Goto first floor and buy windows laptop or mobile")
elif user == 2:
    print("Goto third floor and buy mac laptop or iphones")
elif user == 3:
    print("Goto third floor and buy mac laptop or iphones")
else:
    print("There is only three floors, please select 1 or 2 or 3")


# In[50]:


# 24.Given an age, figure out whether someone's a baby, toddler, child, teenager, adult or old codger.

age = int(input("Enter your age:- "))
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


# In[52]:


# 25.Take two number a,b from the user and check whether a is divisible by b or not

a = int(input("Enter a number1:- "))
b = int(input("Enter a number2:- "))

if b!= 0:
    if a%b == 0:
        print("Yes")
    else:
        print("No")
else:
    print("Zero division error")


# In[54]:


# 26. Take a letter from the user and print that letter belongs to which category I.e is it a small letter or capital letter
# or number or special symbol

user = input("Enter any character only once:- ")
if user.isupper():
    print("Upper case")
elif user.islower():
    print("Lower case")
elif user.isdigit():
    print("Number")
else:
    print("Special character")


# # looping statements

# In[77]:


# 25. Take a number from the user and check whether it is prime?

n = int(input("Enter a number:- "))

if n <= 1:
    print("Not Prime")
else:
    c = 0
    for i in range(1,n+1):
        if n%i == 0:
            c += 1
    if c == 2:
        print("It's Prime")
    else:
        print("Not Prime")
    


# In[79]:


# 26. Take a string from the user and check contains only digits or not?

string = input("Enter input:- ")

if string.isdigit():
    print("Contain only digits")
else:
    print("Does not contain only digits")


# In[14]:


# 27. Take a string from the user and check contains only alphabets or not?
string = input("Enter input:- ")

if string.isalpha():
    print("Contains only alphabets")
else:
    print("Does not contains only alphabets")



# In[15]:


# 28. Take a string from the user and check contains only special chars or not?
string = input("Enter input:- ")
# if all(not i.isalnum() for i in string):
#     print("The string contain only special characters")
# else:
#     print("The string does not contain special characters")

c = 0
for i in string:
    if not i.isalnum():
        c += 1 
if c==len(string):
    print("Contains only speical characters")
else:
    print("Does not contain only special characters")
    
        


# In[4]:


# 29.Take a string from the user and check contains only capital letters or not?

string = input("Enter input:- ")

if all(i.isupper() for i in string):
    print("Contains only capital letters")
else:
    print("Does not contan only capital letters")


# In[6]:


# 30.Take a string from the user and check contains only small letters or not?

string = input("Enter input:- ")

if all(i.islower() for i in string):
    print("Contains only small letters")
else:
    print("Does not contain only small letters")


# In[19]:


'''
31. WAP to replace last n occurrence of give string.
For example:”apple,orange,apple,grape,orange,apple,apple,orange”
source: “apple”
last occurrences: 2
replace with: APPLE
output:”apple,orange,apple,grape,orange,APPLE,APPLE,orange”
'''

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


# In[22]:


# 32. WAP to check given string contains numbers or not. it should consider float numbers also.

string = input("Enter input:- ")
c = 0
for i in string:
    if i.isdigit() or (string.count('.') == 1):
        c += 1
        break
if c == 1:
    print("String contains number")
else:
    print("String does not contains number")


# In[44]:


# 33. Convert the total string in to lower case. Without using lower() function.

string = input("Enter input:- ")
res = ""
for i in string:
    res += chr((ord(i))+32)
print(res)


# In[46]:


# 34. Convert the total string in to upper case. Without using upper() function.

string = input("Enter input:- ")
res = ""
for i in string:
    res += chr(ord(i)-32)
print(res)


# In[47]:


'''
35. Show the below menu to the user until and until user select quit and display corresponding os message
      Menu:

        1. windows
        2. Linux
        3. Mac
        4. quit
'''

while True:
    print("\tMenu:- \n1.windows\n2.Linux\n3.Mac\n4.quit")
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
        


# In[51]:


# 36. Take a string from the user and check contains at least one digit or not?

string = input("Enter input:- ")

for i in string:
    if i.isdigit():
        print("String contains atleast one digit")
        break
else:
    print("String does not contains digit")


# In[53]:


# 37. Take a string from the user and check contains at least one alphabets or not?

string = input("Enter input:- ")

for i in string:
    if i.isalpha():
        print("String contains atleast one alphabets")
        break
else:
    print("String does not contains atleat one alphabets")
        


# In[57]:


# 38. Take a string from the user and check contains at least one chars or not?

string = input("Enter input:- ")

if len(string)>=1:
    print("String contains at least one chars")
else: 
    print("String does not contains at least one chars")


# In[60]:


# 39. Take a string from the user and check contains at least one capital letter or not?

string = input("Enter input:- ")

for i in string:
    if i.isupper():
        print("String contains at least one capital letter")
        break
else:
    print("String does not contains at least one capital letter")
    



# In[61]:


# 40. Take a string from the user and check contains at least one small letter or not?

string = input("Enter input:- ")

for i in string:
    if i.islower():
        print("String contains at least one lower letter")
        break
else:
    print("String does not contains at least one lower letter")


# In[73]:


# 41. Print the first 100 odd numbers
c = 0
res = ""
odd = 1
while 100 > c:
    if odd%2 != 0:
        res += str(odd)+" "
        c += 1
    odd += 1
        
print(res)      


# In[77]:


# 42. Determine the factors of a number entered by the user

user = int(input())
for i in range(1, user+1):
    if user%i == 0:
        print(i)
            


# In[2]:


# 43. Play a number guessing game (User enters a guess, you print YES or Higher or Lower). 
# This should continue until and until user gives a correct number or want to quit in the middle.
# Get a hidden number by using random.randint(1,100)

import random
num = random.randint(1,100)

while True:
    user = input("Enter a guess number in between 1 to 100:- ")
    
    
    if user > str(num):
        print("You have entered higher value")
        
    elif user < str(num):
        print("You have entered lower value")

    elif user == str(num) or user == 'q':
        print("You have gusseed correct number")
        break
    
    u = input("If you want quit press q else enter any:- ")
    if u == 'q':
        break
        


# In[ ]:


# 44. Take two numbers from the user a,b check whether a is divisible by b or not?
a = int(input("Enter a number:- "))
b = int(input("Enter a number:- "))

if a%b == 0:
    print("a is divisible by b")
else:
    print("a is not divisible by b")


# In[9]:


# 45. Find the sum of all the multiples of 3 or 5 below 1000

res = 0
for i in range(1,1001):
    if i%3 == 0 or i%5 == 0:
        res += i
print(res)


# In[8]:


# 46. Write a program to find out big of two numbers

n1 = int(input("Enter input:- "))
n2 = int(input("Enter input:- "))

if n1 > n2:
    print(n1, "is the bigger")
elif n1 == n2:
    print("Both are equal")
else:
    print(n2, "is the bigger ")


# In[6]:


# 47. Write a program to find out biggest number in the given numbers.

l = [122,1,2,4,11,5,6,724,9]
big = 0

for i in l:
    if big < i:
        big = i
        
print(big)        


# In[10]:


# 48. Find out the index of third occurrence of given substring

user_string = input("Enter a string:- ")
sub_string = input("Enter a sub string which we want to find index of substring:- ")

c = 0
for i in range(len(user_string)):
    if user_string[i] == sub_string:
        c += 1
        if c == 3:
            print(i)
            break 
     


# In[28]:


# 49. Find out the index nth occurrence of given substring

user_string = input("Enter a string:- ")
sub_string = input("Enter a sub string which we want to find index of substring:- ")
print(user_string.rfind(sub_string))



# In[29]:


# 50. Take some single digit numbers from the user and findout min, maximum, sum, average

n = list(map(int,input().split()))
print(min(n))
print(max(n))
print(sum(n))
print(sum(n)/len(n))


# In[31]:


'''
51. Print the number in proper mathematical way.
Consider that we have 6 digit numbers.
Number format WAP> 10 -> 000010
100 -> 000100
1000 -> 001000
2345678 -> 2345678
If the number has more than 6 digits then print as it is.
'''

user = input("Enter input:- ")
if len(user) > 6:
    print(user)
else:
    l = len(user)
    s = 6-l
    print(s*"0"+user)


# In[32]:


# 52. Names ="emp1,emp2,emp3,emp4" iterate through the employee names.

user = input().split(",")
for i in user:
    print(i)


# In[2]:


# 53. Take actual string, source string, destination string. replce first nth occurrences of source string with 
# destination string of actual string.

actual_string = input()

source_string = input()
dest_string = input()

row = actual_string[::-1].replace(source_string[::-1], dest_string[::-1],1)
print(row[::-1])


# In[4]:


'''
54. Take a two numbers from the user and do below menu driven operations
     1. addition
     2. multiples 
     3.division
     4.sqrt
     5. pow a**b
     6.subtraction
   After selection do the corresponding operation.

Note: user may give int, or float numbers. You should check whether it is proper digits or not. 
I.e the user given string should be in the position to convert to float. Other wise show the “inproper string given” Error.
'''

n1 = float(input("Enter a number"))
n2 = float(input("Enter a number"))
print("\t Select an option\n1.Add\n2.Sub\n3.Multi\n4.Div\n5.power\n6.sqrt")
user = int(input("Enter your option:- "))

if user == 1:
    print(n1+n2)
elif user == 2:
    print(n1-n2)
elif user == 3:
    print(n1*n2)
elif user == 4:
    print(n1/n2)
elif user == 5:
    print(n1**n2)
elif user == 6:
    print(n1,'=',n1**0.5)
    print(n2,'=',n2**0.5)

else:
    print("Enter proper option")


# In[5]:


# 55. Take numbers from the user and find out min, maximum, sum, average

n = list(map(int,input().split()))
print(min(n))
print(max(n))
print(sum(n))
print(sum(n)/len(n))


# In[24]:


'''
56. l=[1,2,3,5,7,8,9,10,11,12,13,20,22,23,24,25,26,27,20,21,22,4] find out how many even numbers are there and how many 
odd numbers are there and how many positive numbers are there and how many negative numbers are there and how many prime 
numbers are there and how many perfect numbers are there and how many Armstrong numbers are there and how many palindrome 
numbers are there.
'''

l=[1,2,3,5,7,8,9,10,11,12,13,20,22,23,24,25,26,27,20,21,22,4]

count_odd = 0
count_even = 0
count_positive = 0
count_negative = 0
count_prime = 0
count_perfect = 0
count_arm = 0
count_pali = 0

def is_prime(i):
    c = 0
    for j in range(1,i+1):
    
            if i%j == 0:
                c += 1
    if c == 2:
        return True
    else:
        return False
    
def is_prefect(i):
    
    c = 0
    for j in range(1,i+1):
        
        if i%j == 0:
            c += j
    if c == i:
        return True
    else:
        return False
    
def isarm(i):
    w = str(i)
    
    c = 0
    for j in w:
        
        c += int(j)**(len(w))
        
    if i == c:
        return True
    else:
        return False
        
for i in l:
    if i%2 != 0:
        count_odd += 1
        
    if i%2 == 0:
        count_even += 1
    
    if i >= 0:
        count_positive += 1
    
    if i < 0:
        count_negative += 1
    
    prime = is_prime(i)
    if prime:
        count_prime += 1
        
    perfect = is_prefect(i)
    
    if perfect:
        count_perfect += 1
        print(i)
    
    arm = isarm(i)
    
    if arm:
        count_arm += 1
    
    if str(i) == str(i)[::-1]:
        count_pali += 1
print("count_odd=",count_odd)
print("count_even=",count_even)       
print("count_positive=",count_positive)    
print("count_negative=",count_negative)
print("count_arm=",count_arm)
print("count_prime=",count_prime)  
print("count_perfect=",count_perfect)
print("count_pali=",count_pali)


# In[10]:


# 57. Take a string from the user and find out how many digits are there, how many special symbols are there, 
# how many small letters are there, how many caps are there.

user = input()
count_digits = 0
count_special = 0
count_small = 0
count_upper = 0

for i in user:
    if i.isdigit():
        count_digits += 1
    elif i.islower():
        count_small += 1
    elif i.isupper():
        count_upper += 1
    else:
        count_special += 1

print("count_digits=",count_digits)
print("count_small=",count_small)
print("count_upper=",count_upper)
print("count_special=",count_special)


# In[11]:


# 58. Take a char from the user and find out how many number of occurrences are there in given string
user = input("Enter input:- ")
chars = input("Enter a charactor to count:- ")
print(user.count(chars))


# In[14]:


# 59. Take a element from the user and find out how many times the element occurred in given list
list_user = [1,2,34,4,5,6,7,8,9,3,2,4,6,7,8,9,10]
user = int(input("Enter input to count a value:- "))
print("count =",list_user.count(user))


# In[16]:


# 60. Take an element from the user and find out how many number of occurrences are there in given tuple
list_user = 1,2,34,4,5,6,7,8,9,3,2,4,6,7,8,9,10
user = int(input("Enter input to count a value:- "))
print("count =",list_user.count(user))


# In[14]:


# 61. Reverse the string without effecting the special symbols. It involves three variations. Write code for three variations.

# 62.Input: abc123,#$45def6%$^789$%^, output: $%^987%$^6fed54,#$321cba

s = "abc123,#$45def6%$^789$%^"
alpnum = [i for i in s if i.isalnum()]

res_alp_num = ""
res_sp = ""

for i in s[::-1]:
    if not i.isalnum():
        res_sp = i +res_sp 
    else:
        if len(res_sp) > 0:
            res_alp_num += res_sp
            res_sp = ""
        res_alp_num += alpnum[-1]
        alpnum.pop(-1)
print(res_alp_num)


# In[28]:


# 63.Input: abc123,#$45def6%$^789$%^, output: 9876fe,#$d54321%$^cba$%^

s = "abc123,#$45def6%$^789$%^"
alp = [i for i in s if i.isalnum()]
res = ""

for i in s:
    if i.isalnum():
        res += alp[-1]
        alp.pop()
    else:
        res += i
print(res)


# In[29]:


# 64.Inout:"123,#$456%$^789$%^", Output: 321,#$654%$^987$%^ Only numbers has to reverse.

s = "123,#$456%$^789$%^"

dig = ""
res = ""
for i in s:
    if i.isdigit():
        dig += i
    else:
        res += dig[::-1]
        dig = ""
        res += i
print(res)
        


# # FUNCTIONS:

# In[22]:


# 65. Define a function to take person details name and age are mandatory parameters and height weight are optional parameters. 
# If the user willing to pass any other details(like adhar, cell, pan, passport etc..) regarding him then your function should 
# access those details.

def user_details(name,age,height=0,weight=0,*args):
    print(name,age,height,weight,args)

user_details("john",20)


# In[23]:


# 65a. Rewrite above assignments by functions. Can use string functions to solve the string related assignments




# In[25]:


# 65 b. Write a function to check given value is even or not

def check_num(n):
    
    if n%2 == 0:
        return "Even"
    
    else:
        return "Odd"

n = int(input("Enter a number:- "))
num = check_num(n)
print(num)


# In[28]:


# 65 c. Write a function to check given value is prime or not

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


# # STRINGS

# In[29]:


# 67. Take a string from the user and check contains only digits or not?

user = input("Enter input:- ")
if user.isdigit():
    print("The string contains only digits.")
else:
    print("The string does not contain only digits.")


# In[39]:


# 68. Take a string from the user and check contains only alphabets or not?

user = input("Enter input:- ")

if user.isalpha():
    print("The string contains only alphabets.")
else:
    print("The string does not contain only alphabets")


# In[46]:


# 69. Take a string from the user and check contains only special chars or not?

user = input("Enter input:- ")
if all(not i.isalnum() for i in user):
    print("The string contain only special characters")
else:
    print("The string does not contain special characters")


# In[52]:


# 70. Take a string from the user and check contains only capital letters or not?

user = input("Enter input:- ")
if all(i.isupper() for i in user):
    print("The string contain only capital letters")
else:
    print("The string does not contain only capital letters")
   


# In[55]:


# 71. Take a string from the user and check contains only small letters or not?

user = input("Enter input:- ")
if all(i.islower() for i in user):
    print("The string contain only lower letters")
else:
    print("The string does not contain only lower letters")


# In[59]:


# 72. WAP to replace last n occurrence.

actual_string = input()

source_string = input()
dest_string = input()

row = actual_string[::-1].replace(source_string[::-1], dest_string[::-1],1)
print(row[::-1])


# In[64]:


# 73. WAP to check given string contains numbers or not. it should consider float numbers also.

user = input("Enter input:- ")

for i in user:
    if i.isdigit() or user.count(".") == 1:
        print("String contains numbers")
        break
else:
    print("String does not contain numbers")


# In[65]:


# 74. Convert the total string in to lower case. Convert the total string in to upper case.

user = input("Enter input:- ")

print(user.lower())
print(user.upper())


# In[76]:


# 75.Convert every word start letter into caps. Some how title not working if it contains numbers and 
# special symbols in the word

user = input("Enter a words space separated:- ").split()

if all(i.isalpha() for i in user):
    res = ""
    for i in user:
        res += i.title()+" "
    print(res)

else:
    print("Title not working if it contains numbers and special symbols in the word")
# special symbols in the word ")



# In[80]:


# 76.Replace last two occurrences of given source string with destination string
# preserve the delimiter after split.

actual_string = input("Enter actual string:- ")

source_string = input("Enter source string:- ")
dest_string = input("Enter destination string:- ")

row = actual_string[::-1].replace(source_string[::-1], dest_string[::-1],2)
print(row[::-1])


# In[82]:


# 77. Write a program to check given substring is there in actual string or not? (search should be case insensitive)
#     example: act="python is a pure object oriented programing language"

act="python is a pure object oriented programing language"

user = input("Enter substring:- ").islower()

if user in act:
    print('The substring in there in actual string')
else:
    print("The substring is not there in actual string")



# In[83]:


# 78.check whether “pure” is there in act or not.
#    Note: Use in operator

c = 'pure'
if c in act:
    print('The substring in there in actual string')
else:
    print("The substring is not there in actual string")

    


# # DATA STRUCTURES

# In[84]:


# 79. l=[10,20,30,[40,50,60],70,[80,90,20]]. Convert this list as single dimensional list

l=[10,20,30,[40,50,60],70,[80,90,20]]

res = []
for i in l:
    if type(i) == int:
        res.append(i)
    else:
        res.extend(i)
print(res)
        


# In[86]:


# 80. input: "Google" print count of each character

i = "Google"
set_i = set(i)
for item in set_i:
    print(item,"=",i.count(item))


# In[97]:


# 81. Convert n dimensional list to single dimensional list.
a = [[1,2,3,4,5],[5,6,7,7,8],[12,34,45,21,56]]
res = []
[res.extend(i) for i in a]
print(res)


# In[101]:


# 82. l=[1,2,3] just make it as a string.

l=[1,2,3]
res = ""
for i in l:
    res += str(i)
print(type(res),res)


# In[102]:


# 83. l=[1,2,3,[4,5,6],7,[8,9,10]] for single dimensional list

l = [1,2,3,[4,5,6],7,[8,9,10]]
res = []
[res.extend(i) for i in a]
print(res)


# In[169]:


# 84. l=['a','A','b','B','d','D','c','C'] WAP to find out case insensitive count and 
# 85. case insensitive search for an element.

l=['a','A','b','B','d','D','c','C'] 
user = input("Enter input from list:- ")
c = 0
for i in l:
    if i.lower() == user.lower():
        c += 1
print("Count=",c)

user = input("Enter input from list:- ")
for i in l:
    if user.lower() in l:
        print("Have search element in list ")
        break


# In[150]:


# 86. l=['a','A','b','B','d','D','c','C'] sort the list properly

# l=['a','A','b','B','d','D','c','C']
# print(sorted(l,key=lambda x:(x.lower(),x)))

l=['a','A','b','B','d','D','c','C']
l.sort()
print(l)



# In[161]:


# 87. Find the start position of the largest block of repeated characters in a given stringn

s = 'aaaaaabbbccccc'
set_s = set(s)
item = []
for i in set_s:
    row = s.count(i)
    item.append((i,row))
ind = max(item, key=lambda a: a[1])
print(ind)
print(s.index(ind[0]))


# In[116]:


# 88. WAP to find union and intersection of lists.

l1 = [12, 13, 14, 15]
l2 = [12, 13, 14, 15, 16, 1]
print(list(set(l1+l2)))
print(list(set(l1).intersection(set(l2))))


# In[118]:


# 89. input: fun(5) output: [1,2,3,4,3,2,1]

def fun(a):
    
    res = []
    for i in range(1,a):
        res.append(i)
    
    for i in range(1,a-1):
        res.append((a-1)-i)
        
    return res
print(fun(5))       


# In[149]:


# 90. input fun('abc') output: [[],][b][a],,[c],[a,b],[b,c],[c,a],[a,b,c]]
from itertools import combinations

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


# In[170]:


# 91. Remove duplicates from the list: a=[1,2,3,2,3,4,1,,3,4]

a=[1,2,3,2,3,4,1,1,3,4]
print(list(set(a)))


# In[173]:


# 92. l=['1','2','3'] get the sum of the list

l=['1','2','3']
a = [int(i) for i in l]
print(sum(a))


# In[175]:


# 93. l1=[1,2,3,4] l2=[5,6,7,8] sum of two lists

l1=[1,2,3,4] 
l2=[5,6,7,8]
print([sum(i) for i in zip(l1,l2)])


# In[188]:


# 94. Find third max value of element in a list with sorting and without sorting a list.

l = [10,23,43,12,34,56,66,25]
l.sort()
print("Third max value of element with sorting =",l[-3])

k = [10,23,43,12,34,56,66,25]
l = k[:]
for i in range(2):
    l.remove(max(l))
print("Third max value of element without sorting =",max(l))
    
        


# In[75]:


# 95. Input = ["1/1","1/2","1/3","1/4","2/5","2/6","2/8"] Output = [['1/1-4'], ['2/5-6'], ['2/8']]

l = ["1/1","1/2","1/3","1/4","2/5","2/6","2/8"] 

num = []
den = []
for item in l:
    num.append(int(item[0]))
    den.append(int(item[2]))



# In[64]:


# 96.l=[1,2,3,5,7,8,9,10,11,12,13,20,22,23,24,25,26,27,20,21,22,4] 
# output = [[1, 2, 3], [5], [7, 8, 9, 10, 11, 12, 13], [20], [22, 23, 24, 25, 26, 27], [20, 21, 22], [4]]

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
    


# In[193]:


# 97. input = 1,2,3,4,5,6,8,10 output = odd,even,odd,even,odd,even,even,even

ip = 1,2,3,4,5,6,8,10
row = ["odd" if i%2 != 0 else "even" for i in ip ]
print(tuple(row))


# In[207]:


# 98. input n=3
#     output: 111 101 111
n = 3
for i in range(n):
    if i == 0 or i == (n-1):
        print('1'*n)
    else:
        s = '1'
        e = '1'
        r = n-2
        z = '0'*r
        print(s+z+e)


# In[216]:


# 99. input: Google
#     output: {'g':2,'o':2,'l':1,'e':1} use dictionary comprehension

ip = "Google".lower()

k = {}
row = {i:ip.count(i) for i in set(ip)}
print(row)


# In[218]:


# 100. keys=['k1','k2'], values = ['v1','v2'] form a dictionary.

keys=['k1','k2']
values = ['v1','v2']

row = {keys[i]:values[i] for i in range(len(keys))}
print(row)


# In[223]:


# 101. Sort the list marks = [("mohan", 80), ("satish", 90), ("purnesh", 40), ("venkat", 30)] 
# according to descending order of marks

list_marks = [("mohan", 80), ("satish", 90), ("purnesh", 40), ("venkat", 30)] 

row = sorted(list_marks, key=lambda x : x[1], reverse=True)
print(row)


# In[244]:


# 102.Write a function to get dynamic list for floating numbers also based on strat and end and step parameters

s = 1
e = 13.2
step = 1.2
res = []

while e > s:
    res.append(round(s,2))
    s += step
print(res)


# In[17]:


# 103. Find out all perfect numbers in given range

def find_perfect(n):
    s = sum(filter(lambda x: n%x == 0, range(1,n)))
    return  s == n
         

start = 1
end = 100000
perfect = list(filter(lambda n : find_perfect(n), range(start, end+1)))
print(perfect)



# In[275]:


# 104. WAP to do all stack operations using lists

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



# In[9]:


# 105.WAP to do all queue operations using lists

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
             


# In[40]:


# 106. WAP to remove n occurrences of specified element from a list

l = [1,2,34,2,3,4,5,6,7,8,9,2,4,6,8,9]
first = int(input("Enter element to remove:- "))
count = int(input("Enter occurrences:- "))
l = l[::-1]
for i in range(count):
    index = l.index(first)
    l[index] = -1
    l.pop(index)
print(l[::-1])


# In[15]:


# 107. Compare two lists ignore order. i.e return True l1=[1,2,3,4],l2=[4,2,3,1], fun(l1,l2)-> True

def fun(l1,l2):
    print(sorted(l1) == sorted(l2))

l1=[1,2,3,4]
l2=[4,2,3,1]
fun(l1,l2)


# In[21]:


# 108. XOR operation in python.
print(bool(1^1))
print(bool(0^1))
print(bool(1^0))
print(bool(0^0))


# In[23]:


# 109. How to remove all occurrences of the given element in a list

l = [1,2,34,2,3,4,5,6,7,8,9,2,4,6,8,9]
l.clear()
print(l)


# In[36]:


# 110. How to remove first n occurrences of the given element in a list

l = [1,2,34,2,3,4,5,6,7,8,9,2,4,6,8,9]
first = int(input("Enter element to remove:- "))
count = int(input("Enter occurrences:- "))

for i in range(count):
    index = l.index(first)
    l[index] = -1
    l.pop(index)
print(l)



# In[38]:


# 111. How to remove last n occurrences of the given element in a list

l = [1,2,34,2,3,4,5,6,7,8,9,2,4,6,8,9]
first = int(input("Enter element to remove:- "))
count = int(input("Enter occurrences:- "))
l = l[::-1]
for i in range(count):
    index = l.index(first)
    l[index] = -1
    l.pop(index)
print(l[::-1])


# In[39]:


# 112. How to remove nth occurrences of the given element in a list

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


# In[44]:


# 113. WAP to generate list of floats i.e: fun(0,1,0.1), [0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]

def fun(a,b,c):
    res = []
    while b > a:
        res.append(round(a,2))
        a += c  
    print(res)
        
fun(0,1,0.1)


# In[45]:


# 114. WAP to remove all occurrences of given substring from actual string

actual_string = "apple orange apple mango grapes apple grapes apple banana"
substring = "apple"
print(actual_string.replace(substring,""))


# In[46]:


# 115. WAP to remove first n occurrences of given substring from actual string

actual_string = "apple orange apple mango grapes apple grapes apple banana"
substring = "apple"
n = int(input("Enter number of occurrences:- "))
print(actual_string.replace(substring,"",n))


# In[57]:


# 116. WAP to remove last n occurrences of given substring from actual string

actual_string = "apple orange apple mango grapes apple grapes apple banana"
a = actual_string[::-1]
substring = "apple"
s = substring[::-1]

n = int(input("Enter number of occurrences:- "))
r = a.replace(s,"",n)
print(r[::-1])


# In[59]:


# 117. WAP to replace last n occurrences of given substring with destination string in actual string
actual_string = "apple orange apple mango grapes apple grapes apple banana"
substring = "apple"
dest_string = input("Enter destination string:- ")
n = int(input("Enter occurrences:- "))
a = actual_string[::-1]
s = substring[::-1]
d = dest_string[::-1]

res = a.replace(s,d,n)
print(res[::-1])


# In[61]:


# 118. WAP to sort the string.
s = "apple"
print("".join(sorted(s)))


# In[62]:


# 119. Take a coma separated numbers and find out max number.

n = [12,34,45,67,43]
print(max(n))


# In[73]:


# 120. Read a json file. Try to get the information from the file
import json

with open("person.json","r") as f:
    data = json.load(f)
print(data)


# In[80]:


# 121.Read a yaml file. Try to get the information from the file

import yaml
#print(dir(yaml))
with open("yamal.yaml","r") as f:
    data = yaml.safe_load(f)
print(data)


# In[82]:


# 122.Read any image data using Opencv




# In[86]:


# 123.Make alternative words reversed in given string:
# ex: "python program good language"-> "python margorp good egaugnal"

word = "python program good language".split()

res = ""
for i in range(len(word)):
    if i%2 != 0:
        res += word[i][::-1]+" "
    else:
        res += word[i]+" "
print(res)
    


# In[90]:


# 124. l=['c',"cpp","java","php","python"]
#      case insensitive count# l.count("C")->1
#      like count l.own_count("c")->2 with case insensitive

l=['C',"cpp","java","php","python"]
res = "".join(l)
user1 = input("Enter charactor to count case sensitive:- ")
user2 = input("Enter charactor to count case insensitive:- ")

res1 = res.count(user1)
new = res.lower()
res2 = new.count(user2)

print("Count of case sensitive:-", res1)
print("Count of case insensitive:-", res2)


# In[123]:


'''
125: Take total parameters, out of which few are optional and few are mandatory. Take some parameters from the user
    and check whether the user given all the mandatory paramerters or not.
    
    For example: to insert person details
    Total parameters: name,age,height,pan,cell,adhar,passport

    mandatory: name,cell,adhar
    if the user given: name,adhar,passport then you need to print cell is mandatory parameter
    if the user given: name,cell,adhar,passport then you need to print ok
    if the user given: adhar,passport then you need to print cell,name are mandatory parameter
'''

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
        


# In[12]:


'''
STRINGS

Take two inputs from the user: your program should check for below scenarios.
10,20: 30
12.34,45.67: 58.01
+12,-12: 0
qwe,23we: Enter digits or float values only

'''

try:
    a,b = map(float, input("Enter values separated by comma:- ").split(","))
    print(sum([a,b]))
except ValueError as err:
    print(err,"please enter int or float values")



# In[77]:


# 116. Take the number of employees count from the user and ask the inputs required for the bmi for each and every person. 
# The result should be like below
# empid:{“weight:”,”height”:,”age”:,”bmi”:0.9,”result”:”+ve”}

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
        
    


# In[78]:


'''
117. CRM: app.py(define a menu: 1.meetings, 2. customer, 3. quit
1:
a. create meeting
b. update meeting
c. delete meeting
d. get the meeting
2:
a. create customer
b. update customer
c. delete customer
d. get the customer
), meetings.py, customer.py
'''


# # FILES

# In[ ]:


# 118. Copy 1 file content in to another file(Take the source and destination file path from the user)




