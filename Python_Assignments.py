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


# In[ ]:


''' 1. Write a class(DB) program to create a table, insert values, update values, delete values of the table.
All database operations code write in a file(db_operations.py) and call these operations in another file( app.py).
In app.py create instance of the DB class and call all the methods by passing some data.
'''

