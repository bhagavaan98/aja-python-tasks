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
    

    


# In[13]:


# Take input from the user
total_people = int(input("Enter total number of people: "))
total_buses = int(input("Enter total number of buses: "))
seats_per_bus = int(input("Enter number of seats for each bus: "))
adjust_factor = int(input("Enter adjust factor: "))

# Calculate the total seats available
total_seats = total_buses * seats_per_bus

# Check if there are sufficient buses
if total_people <= total_seats:
    print("There are sufficient buses.")
else:
    # Calculate the required extra buses
    extra_buses_required = (total_people - total_seats + adjust_factor - 1) // adjust_factor
    print(f"Additional {extra_buses_required} buses are required.")


# In[ ]:





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
    
        
    


# In[45]:


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
    else:
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
    else:
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


# In[33]:


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
            


# In[ ]:


# 43. Play a number guessing game (User enters a guess, you print YES or Higher or Lower). 
# This should continue until and until user gives a correct number or want to quit in the middle.
# Get a hidden number by using random.randint(1,100)
#To slove the problem

