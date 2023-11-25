#!/usr/bin/env python
# coding: utf-8

# In[3]:


""" Take the input from the user for(Total number of people,Number of seats for bus. Based on two
inputs
Decide how many number of buses required"""

x = int(input())
y = int(input())

busses = x // y 

if x % y != 0:
    busses = busses + 1 
print(busses)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[9]:





# In[4]:


temp = int(input())
F = (temp * (9 / 5)) + 32 
print(F,"F")


# In[6]:


temp = int(input())
c = (temp - 32) * 5/9 
print(c ,"C")


# In[ ]:





# In[ ]:


from math import  sqrt
x1,x2,x3,x4 = list(map(int,input().split()))
v1 = (x1+x2)**2
v2 = (x3+x4)**3

total = sum([x1,x2,x3,x4])
avg = total // 4 
variance = (x1-avg) ** 2 + (x2-avg) ** 2 + (x3-avg) ** 2 + (x4-avg) ** 2 
sqr_of_variance = sqrt(variance)



# In[ ]:


from math import  sqrt
x1,x2,x3,x4 = list(map(int,input().split()))
v1 = (x1+x2)**2
v2 = (x3+x4)**3

total = sum([x1,x2,x3,x4])
avg = total // 4 
variance = (x1-avg) ** 2 + (x2-avg) ** 2 + (x3-avg) ** 2 + (x4-avg) ** 2 
sqr_of_variance = sqrt(variance)
Y = 1.23 * (total) + 0.045
print(total,avg,variance,sqr_of_variance,Y)



# In[ ]:





# In[1]:


distance = int(input())
print(distance * 100000 , "cm")
print(distance * 1000 , "m")
print(distance * 1000000. , "mm")
print(distance * 24715.769 , "cents")
print(distance * 3280.84 , "feets")


# In[ ]:


GB = int(input())
print(Gb * 1000 ,'MB')
print(Gb * 1000000 ,'KB')
print(Gb * 0.001 ,'TB')
print(Gb * 10 ** (-6) ,'PB')


# In[ ]:





# In[ ]:


GB = int(input())
print(Gb * 1000 ,'MB')
print(Gb * 1000000 ,'KB')
print(Gb * 0.001 ,'TB')
print(Gb * 10 ** (-6) ,'PB')


# In[2]:


name = input()
age = int(input())
height = input()
print(f"Name:{name}, Age:{age}, Height:{float(height)}")


# In[3]:


weight = int(input())
height = float(input())
print(weight/ (height * height))


# In[7]:


name=&quot;Jayaram&quot;
age=1.6
height=3.5356234
weight=10.343856783
print('Name:%s, Age:%f, Height:%f, Weight:%f'%(name,age,height,weight))


# In[9]:


name ="lakshmi Kanth"
age=1.6
height=3.5356234
weight=10.343856783
print('Name:%s, Age:%f, Height:%f, Weight:%f'%(name,age,height,weight))


# In[11]:


"""  Take three upper case letters from the user convert in to small case.  """
a = input()
print(a.lower())


# In[12]:


"""take base and exponent value from the user and print like in mathematics:"""
base = int(input())
exponent = int(input())
print()


# In[14]:


""" Take some groceries cost prices and print total cost and average cost, what is the max cost, what is
the minimum cost. """


soap = int(input())
suger = int(input())
choclate = int(input())

total = sum([soap,suger,choclate])
avg = total/3
maximum = max([soap,suger,choclate])
minimu = min([soap,suger,choclate])

print(f"total :{total} , avg :{avg} , maximum :{maximum} , minimum:{minimu}")






# In[15]:


a = input()

if a:
    print("ten")
else :
    print("not ten")
    


# In[ ]:


""" Assign “ten” value to variable it is 10 otherwise assign “Not ten” """
a = input()

if a:
    print("ten")
else :
    print("not ten")


# In[17]:


""" Take the input from the user for(Total number of people, total number of buses, Number of
seats for bus, adjust factor). Based on four inputs
Decide whether there is sufficient buses or not and give solution for how many extra buses
required. """


people = int(input())
busses = int(input())
seats = int(input())
adjust_factor = int(input())


total_no_seats = busses * seats * adjust_factor 

n = people // total_no_seats 

if n > 0:
    print(f"no_of_busses_required :{n}")
else :
    print("sufficient busses")








# In[ ]:


"""  14.Take number from the user decide whether it is even or odd. """


a = int(input())

if a % 2 == 0:
    print("even")
else :
    print("odd")




# In[19]:


"""  16.take a string from the user print the length. if the user not given anything then show an error
message  """

try  :
    a = input()
    print(len(a))
    
except EOFError :
    print("Please enter the input")



# In[ ]:


"""  17.code to perform mathematical operations. take two numbers from the user and show the
below menu
1. add,
2. sub,
3. mul,
4.div,
5.quit
Enter an option:
based on the option need to perform an operations """


def add():
    print(10+20)
def sub():
    print(20-10)
def mul():
    print(20*10)
def div():
    print(20//10)
    
a = input()

    
function = [add,sub,.mul,div]
names = ["add","sub","mul","div"]
for i in zip(function,name):
    print(i)



# In[ ]:


def add():
    print(10+20)
def sub():
    print(20-10)
def mul():
    print(20*10)
def div():
    print(20//10)
    
a = input()

    
function = [add,sub,.mul,div]
names = ["add","sub","mul","div"]
for i in zip(function,name):
    print(i)
print("ok")




# In[1]:


""" write a program to chcek given substring is there in actual string or not?
example: act=&quot;python is a pure object oriented programing language&quot;
check whether “pure” is there in act or not.
Note: Use in operator """

act="python is a pure object oriented programing language&quot"

print("pure" in act.split())


# In[ ]:


a = int(input())
b = int(input())
c = int(input())

e = lambda a,b,c : a if a>c else c if a>b else b if b > c else c
e(a,b,c)


# In[8]:


age = int(input())
gender = input()


k = lambda age,gender :"he is eligible" if age > 24 else "he is not eligale" if gender == "M" else "she if eligable" if age > 21 else "she is not eligable"
k(age,gender)


# In[ ]:


""" 22. Take an age and gender from the user: and mention that what he/she can do in india.
&quot;&quot;&quot;
conditions
1. Theatre: 5 for men 7 for women
2. Voting system: 18 for men and women
3. Marriage in india: 23 for men and for women &gt;21
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
Enter an age of person: """ 




gender = input()
age = int(input())



Theater = lambda gender,age :  "He Theater eligable" if age > 7  else "He theater not eligable"  if gender == "men" else "He Theater eligable" if age > 5  else "He theater not eligable"
print(Theater(gender,age))

Voting = lambda gender,age : "Voting eligable"  if age >= 18 else "Not eligable"
print(Voting(gender,age))

Marriage = lambda gender,age :  "He Marriage eligable" if age > 23  else "He marriage not eligable"  if gender == "men" else "She Marriage eligable" if age > 21  else "SHe marriage not eligable"
print(Marriage(gender,age))


Govt_jobs = lambda gender,age :  "He  eligable govt_jobs" if age >= 18 and age <= 32  else "He  eligable govt_jobs"  if gender == "men" else "she  eligable govt_jobs" if age >= 18 and age <= 34  else "sHe  eligable govt_jobs"
print(Govt_jobs(gender,age))


# In[14]:


"""operating systems:

1.windows
2.android
3.mac
Enter an option:

If the user enters 1 then show &quot;Goto first floor and buy windows laptop or mobile&quot;
If the user enters 2 then show &quot;Goto second floor and buy adroid mobiles&quot;
If the user enters 3 then show &quot;Goto third floor and buy mac laptop or iphones&quot;
If the user enters other than 1 or 2 or 3 then show &quot;There is only three floors, please select 1 or
2 or 3&quot; """





a = int(input())

if a == 1:
    print("Goto first floor and buy windows laptop or mobile")

elif a == 2:
    print("Goto second floor and buy adroid mobiles")
elif a == 3:
    print("Goto third floor and buy mac laptop or iphones&quot")

else :
    print("There is only three floors, please select 1 or 2 or 3")



# In[ ]:


"""  Take a letter from the user and print that letter belongs to which category I.e is it a small letter or
capital letter or number or special symbol """

a = input()

if ord("A") <= ord(a) >= ord("Z"):
    print("Capital")
    
elif ord("a") <= ord(a) >= ord("z"):
    print("Small")
else :
    print("number")


# In[17]:


""" take a string from the user and check contains only digits or not? """

a = input()
print(a.isnumeric())


# In[ ]:


""" take a string from the user and check contains only special chars or not? """
a = input()
if a.isalpha():
    print("str contains no spectial charecter")
else :
    print("str contains spectial charecter")


# In[ ]:


""" Convert the total string in to lower case. Without using lower() function. """

a = input()
str = ""

for i in a :
    if i == i.upper():
        i = chr(ord(i) + 32)
    str = str + i 
print(str)


# In[20]:


"""Find the sum of all the multiples of 3 or 5 below 1000"""
print(sum([i for i in range(1000) if i%3 ==0 and i%5==0]))


# In[ ]:


""" find out the index of third occurrence of given substring """

a = input()
b = "a"

count = 0 
index = 0
for i in a:
    if i == b :
        count = count + 1 
        if count == 3:
            
            break
            
    index = index + 1
print(index-1)


# In[3]:


"""  Take a letter from the user and print that letter belongs to which category I.e is it a small letter or
capital letter or number or special symbol """
a = input()
if ord("a") <= ord(a) >= ord("z"):
    print("it is small")
elif ord("A") <= ord(a) >= ord("Z"):
    print("it is capital")
else:
    print("it special char")


# In[ ]:


"""  31. WAP to replace last n occurrence of give string.
For example:”apple,orange,apple,grape,orange,apple,apple,orange”
source: “apple”
last occurrences: 2 """


a = input().split(",")
b = input()
reverse_of_a = a[::-1]
c = 0 
print(reverse_of_a)
for i,j in enumerate(reverse_of_a):
  
    if j == b:
        c = i + 1
        
        while True:
            if reverse_of_a[c] == b:
                c = c + 1 
                print(c-1)
            else :
                break 
        break



# In[ ]:


"""  41. Print the first 100 odd numbers """

print(len([i for i in  range(1,201) if i % 2 != 0 ]))


# In[ ]:


a = int(input())

print([i for i in range(1,a+1) if a % i ==0 ])


# In[ ]:


""" Take two numbers from the user a,b check whether a is divisible by b or not? """

a = int(input())
b = int(input())
if a % b == 0:
    print("divisible")
else :
    ("Not")


# In[ ]:


""" 45. Find the sum of all the multiples of 3 or 5 below 1000 """
print(sum([i for i in range(1,1001) if i % 3 ==0 or i % 5 ==0  ]))


# In[ ]:


""" Write a program to find out big of two numbers """

a = int(input())
b = int(input())

if a > b:
    print(a)
else :
    print(b)


# In[ ]:


""" names = "emp1,emp2,emp3,emp4" iterate through the employee names. """

names = "emp1,emp2,emp3,emp4"

for name in names.split(","):
    print(name)


# In[ ]:


""" 56. l=[1,2,3,5,7,8,9,10,11,12,13,20,22,23,24,25,26,27,20,21,22,4] find out how many even
numbers are there and how many odd numbers are there and how many positive numbers are
there and how many negative numbers are there and how many prime numbers are there and
how many perfect numbers are there and how many Armstrong numbers are there and how
many palindrome numbers are there. """



l=[1,2,3,5,7,8,9,10,11,12,13,20,22,23,24,25,26,27,20,21,22,4]

even = [i for i in l if i % 2 == 0]
odd = [i for i in l if i % 2 != 0]
poss = [i for i in l if i >= 0 ]
negative = [i for i in l if i < 0 ]
prime = []

for i in l:
    c = 0 
    for j in range(1,i+1):
        if i % j == 0:
            c = c + 1 
    if c > 2 :
        prime.append(i)

print(prime)

Armstrong = []

for i in l:
    i = str(i)
    sum = 0 
    for j in i:
        j = int(j)
        sum = sum + j ** len(i)
    if sum == i :
        Armstrong.append(i)



# In[ ]:


"""  Take a char from the user and find out how many number of occurrences are there in given
string """

string = input()
char = input()
print(string.count(char))


# In[ ]:


from random import randint
number = randint(1,100)
while True:
    u = input()
    if u.isalnum():
        if int(u) > number:
            print("Greater")
        elif int(u) < number:
            print("Smaller")
        elif int(u) == number:
            print("congrats")
        
    elif u == "q":
        break
   


# In[1]:


"""  79. l=[10,20,30,[40,50,60],70,[80,90,20]]. Convert this list as single dimensional list"""

l=[10,20,30,[40,50,60],70,[80,90,20]]

res = []

for i in l:
    if type(i) == type(1):
        res.append(i)
    else :
        for j in i:
            res.append(j)
print(res)


# In[ ]:





# In[ ]:


""" WAP to check given string contains numbers or not. it should consider float numbers also. """

a = input()

c = 0 

for i,j in enumerate(a):
    if j == ".":
        if a[i-1].isdigit() and a[i+1].isdigit():
            
            c = c + 1 
    elif j.isdigit():
        c = c + 1 
    
if c > 0:
    print("given sting has numbers")
else :
    print("given sting has no numbers")

""" WAP to find union and intersection of lists. """ 

a = [1,2,4,6,7,3]
b = [10,2,6,4,9,13]

intersection = []
union = a 
for i in b:
    if i not in union:
        union.append(i)
    
print(union)
for i in a:
    if i in b:
        intersection.append(i)
print(intersection)


""" input fun('abc') output: [[],][a],[b],[c],[a,b],[b,c],[c,a],[a,b,c]] """



from itertools import combinations

a = "abc"
ran = len(a)

com = combinations([0,1,2],2)

for i in range(len(a)):
    com = combinations(a,i+1)
    for j in com:
        print(j)
  

""" Remove duplicates from the list: a=[1,2,3,2,3,4,3,4] """ 
a=[1,2,3,2,3,4,3,4]


for i in a[::-1]:
    if a.count(i) > 1 :
        a.remove(i)
print(a)


""" l=["1","2","3"] get the sum of the list """
l=["1","2","3"]
c = lambda x : int(x)
print(sum(list(map(c,l))))

""" l1=[1,2,3,4] l2=[5,6,7,8] sum of two lists """ 
l1=[1,2,3,4] 
l2=[5,6,7,8]
res = []
for i in zip(l1,l2):
    res.append(sum(i))
print(sum(res))


""" Find third max value of element in a list with soring and without sorting a list. """

a = [1,2,6,5,7,3,9,10]



for i in a:
    count = 0 
    for j in a:
        if i > j:
            count = count + 1 
    if count == 3:
        print(i)
        break


# In[ ]:


""" WAP to check given string contains numbers or not. it should consider float numbers also. """

a = input()

c = 0 

for i,j in enumerate(a):
    if j == ".":
        if a[i-1].isdigit() and a[i+1].isdigit():
            
            c = c + 1 
    elif j.isdigit():
        c = c + 1 
    
if c > 0:
    print("given sting has numbers")
else :
    print("given sting has no numbers")

""" WAP to find union and intersection of lists. """ 

a = [1,2,4,6,7,3]
b = [10,2,6,4,9,13]

intersection = []
union = a 
for i in b:
    if i not in union:
        union.append(i)
    
print(union)
for i in a:
    if i in b:
        intersection.append(i)
print(intersection)


""" input fun('abc') output: [[],][a],[b],[c],[a,b],[b,c],[c,a],[a,b,c]] """



from itertools import combinations

a = "abc"
ran = len(a)

#com = combinations([0,1,2],2)

for i in range(len(a)):
    com = combinations(a,i+1)
    for j in com:
        print(j)
  

""" Remove duplicates from the list: a=[1,2,3,2,3,4,3,4] """ 
a=[1,2,3,2,3,4,3,4]


for i in a[::-1]:
    if a.count(i) > 1 :
        a.remove(i)
print(a)


""" l=["1","2","3"] get the sum of the list """
l=["1","2","3"]
c = lambda x : int(x)
print(sum(list(map(c,l))))

""" l1=[1,2,3,4] l2=[5,6,7,8] sum of two lists """ 
l1=[1,2,3,4] 
l2=[5,6,7,8]
res = []
for i in zip(l1,l2):
    res.append(sum(i))
print(sum(res))


""" Find third max value of element in a list with soring and without sorting a list. """

a = [1,2,6,5,7,3,9,10]



for i in a:
    count = 0 
    for j in a:
        if i > j:
            count = count + 1 
    if count == 3:
        print(i)
        break


# In[ ]:


""" input: Google"""
word = "Google"
word_2 = ""
for i in word:
    if i not in word_2:
        word_2 = word_2 + i 
res = { i:word.count(i) for i in word_2}
print(res)


# In[ ]:


""" 101. Sort the list marks = [("mohan", 80), ("satish", 90), ("purnesh";, 40), ("venkat";, 30)]
according to descending order of marks """


marks = [("mohan", 80), ("satish", 90), ("purnesh", 40), ("venkat", 30)]

c = lambda x : (x[1],x[0])

print(sorted(list(map(c,marks)),reverse=True))


# In[ ]:


"""  102.write a function to get dynamic list for floating numbers also based on strat and end and
step parameters """

start = int(input())
end = int(input())
step = float(input())

res = []

while True:
    if start >= end:
        break
    start = start + step
    start = round(start,1)
    res.append(start)
    
print(res)
    

