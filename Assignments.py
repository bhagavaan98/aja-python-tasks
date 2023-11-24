#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#1.Take the input from the user for(Total number of people, Number of seats for bus. Based on two inputs 
#Decide how many number of buses required 
p=int(input())
s=int(input())
b=p//s 
if ((p%s)!=0):
    print(b+1)
else:
    print(b)


# In[ ]:


#2.take temperature from the user and convert foreign heat -> Celsius. 
F=int(input())
celsius=(F-32)*(5/9)
print(str(celsius)+"C")


# In[ ]:


#3.take temperature from the user and convert Celsius → foreign heat.
c=int(input())
Foreign_heat=(9*c/5)+32
print(str(Foreign_heat)+"F")


# In[7]:


#4.
a,b,c,d = map(int,input().split())
res1 = (a+b)**2
res2 = (c+d)**3
mean = (a+b+c+d)/4
varience = ((a-mean)**2 + (b-mean)**2 + (c-mean)**2 + (d-mean)**2)/4
std_dev = (varience)**(0.5)
y = 1.23*(a+b+c+d)+0.045
avg = mean
sum_of_four = a+b+c+d
print(res1)
print(res2)
print(varience)
print(std_dev)
print(y)
print(avg)
print(sum_of_four)


# In[ ]:


#5.Take the distance in km  Show that in cm, meters, in milli meters, cents, feets, yards 
km=int(input())
m=km*1000
cm=km*1000*100
mm=km*1000*1000
cents=40.4686*(m*m)
feet=(0.002296169)**0.5
yards=3*feet
print(str(m)+"m")
print(str(cm)+"cm")
print(str(mm)+"mm")
print(str(cents)+"cents")
print(str(feet)+"feet")
print(str(yards)+"yards")


# In[ ]:


#6.Take the size of your hard disk in GB Show that in MB, KB, TB, PB 
GB=int(input())
MB=GB*1000
KB=MB*1000
TB=GB/1000
PB=TB/1000
print(MB)
print(KB)
print(TB)
print(PB)


# In[ ]:


'''' #7.Take name, age, height from the user and print like below 

The details of the person: Name:name of the person, Age:age of the person, Height:height of the person 

Note: make sure that no space between : and a value and should be space after “COMA” 
''''

name=input()
age=input()
height=input()
print("The details of the person: "+"Name:"+name+", "+"Age:"+str(age)+", "+"Height:"+str(height))


# In[1]:


#8.BMI calculation: take required parameters for BMI calculation from the user and calculate BMI of the person. 
weight=int(input())
height=int(input())
BMI=weight/((height**2))
print(BMI)


# In[11]:


'''9.. name="Jayaram" 

age=1.6 

height=3.5356234 

weight=10.343856783 

By using above inputs print the output 

Name:Jayaram, Age:1.6, Height:3.54, Weight:10.344 

Note: Use format specifiers(%s, %d, %f) 
'''
name=input()
age=float(input())
height=float(input())
weight=float(input())
info = "Name: %s, Age: %f, Height: %f, Weight: %f"%(name, age, height, weight)
print(info)


# In[ ]:


#10.Take three upper case letters from the user convert in to small case.
a=input()
b=a.lower()
print(b)


# In[2]:


#11. take base and exponent value from the user and print like in mathematics: example: base=2, exponent=3: 23 
print(f'2\u00b3')


# In[ ]:


#12.Take some groceries cost prices and print total cost and average cost, what is the max cost, what is the minimum cost. 
a=list(map(int,input().split()))
b=len(a)
print(sum(a))
print(sum(a)/b)
print(max(a))
print(min(a))


# In[5]:


##13Assign “ten” value to variable it is 10 otherwise assign “Not ten”  Note: write two versions of program  Version1: use and operator  Version2: use or operator  
a=int(input())
if a==0:
    print(a or 10 )
else:
    print("Not ten")


# In[ ]:


a=int(input())
if a!=0:
    print(a and 10)
else:
    print("Not ten")


# In[1]:


#13 conditional statements Take the input from the user for(Total number of people, total number of buses, Number of seats for bus, adjust factor). Based on four inputs 

#Decide whether there is sufficient buses or not and give solution for how many extra buses required. 
total_no_of_people=int(input("enter total_no_of_people"))
total_no_of_buses=int(input("enter total_no_of_buses"))
no_of_seats_per_bus=int(input("no_of_seats_per_bus"))
adjust_factor=int(input("enter adjust factor"))
total_no_of_seats=total_no_of_buses*no_of_seats_per_bus 
remaining_people=(total_no_of_people)-(total_no_of_seats)
update_adjust_factor=(remaining_people)-(adjust_factor)
if update_adjust_factor>0:
    print(f'required_sufficient_buses =  {round(update_adjust_factor/no_of_seats_per_bus)}')
else:
    print("sufficient_buses")



# In[ ]:


#14 Take number from the user decide whether it is even or odd. 
a=int(input())
if a%2==0:
    print("Even")
else:
    print("Odd")


# In[ ]:


#15 take number from the user decide whether it is positive number or negative number 
a=int(input())
if a>=0:
    print("positive")
else:
    print("Negative")


# In[ ]:


#16 take a string from the user print the length. if the user not given anything then show an error message 
a=input()
if a!="":
    print(len(a))
else:
    print("Error message")


# In[10]:


'''''17code to perform mathematical operations. take two numbers from the user and show the below menu 

1. add, 

2. sub,	 

3. mul, 

 	4.div,  

5.quit 

Enter an option: 

based on the option need to perform an operations 
''''
a=int(input())
b=int(input())
c=int(input("enter an option for add=1,sub=2,mul=3,div=4,quit=5"))
if c==1:
    print(a+b)
elif c==2:    
    print(abs(a-b))
elif c==3:
    print(a*b)
elif c==4:
    print(a/b)
elif c==5:
    print("quit")
    


# In[ ]:


'''''18. show the menu: 

   		 1. kids 

    		2. Men's 

   		 3. Women's 

    		Show the corresponding message based on the selection. 

Option:1: you are a kid 

                                           2: you are a gentlemen 

                                            3: you are a good women 

 

 Mention error message if the option value >3. 
''''
print("enter below options\n 1.kids\n 2.Men's\n 3.women's")
a=int(input())
if a==1:
    print("you are a kid")
elif a==2:
    print("you are a gentlemen")
elif a==3:
    print("you are a good women")


# In[ ]:


'''' 19.write a program to chcek given substring is there in actual string or not? 

example: act="python is a pure object oriented programing language" 

check whether “pure” is there in act or not. 

Note: Use in operator 
''''
a=input()
b=input()
if b in a:
    print("string is there")
else:
    print("string is not there")


# In[4]:


#20 Take three numbers from the user and decide which is big 
a=int(input())
b=int(input())
c=int(input())
if a>b and a>c:
    print(a)
elif b>a and b>c:
    print(b)
else:
    print(c)


# In[5]:


#21 Take age and gender from the user and decide whether he is eligible for 	marriage in India or not. Age criteria: men age>24, women>21 
age=int(input())
gender=input()
if (gender=="men" and age>24) or (gender=="women" and age>21):
    print("eligible for marriage")
else:
    print("not eligible for marriage")


# In[11]:


''''' 22 Take an age  and gender from the user: and mention that what he/she can 	do in india. 

""" 

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

Enter an age of person: 
'''
gender=input("enter gender:\n 1.men\n 2.women\n")
age=int(input("enter age\n"))
if (gender=="1" and age>=5) or (gender=="2" and age>=7):
    print("eligible for Theatre")
if (gender=="1" and age>=18) or (gender=="2" and age>=18):
    print("eligible for Voting system")
if (gender=="1" and age>=23) or (gender=="2" and age>=21):
    print("eligible for marriage")
if (gender=="1" and ((age>=18) and (age<=32))) or (gender=="2" and ((age>=18) and (age<=34))):
    print("eligible for government jobs")
if (gender=="1" or gender=="2") and ((age>=18) and (age<=60)):
    print("eligible for Theatre")    


# In[13]:


''''23 operating systems: 

1.windows 

2.android 

3.mac 

Enter an option: 

 

If the user enters 1 then show "Goto first floor and buy windows laptop or mobile" 

If the user enters 2 then show "Goto second floor and buy adroid mobiles" 

If the user enters 3 then show "Goto third floor and buy mac laptop or iphones" 

If the user enters other than 1 or 2 or 3 then show "There is only three floors, please select 1 or 2 or 3" 
''''
user=int(input("enter below options \n 1.windows\n 2.android \n 3.mac \n"))
if user==1:
    print("Goto first floor and buy windows laptop or mobile")
elif user==2:
    print("Goto second floor and buy android mobiles")
elif user==3:
    print("Goto third floor and buy mac laptop or iphones")
elif user>3:
    print("There is only three floors,please select 1 or 2 or 3")


# In[14]:


#24.Given an age, figure out whether someone's a baby, toddler, child, teenager, adult or old codger. 
age = int(input("Enter your age \n"))
if age <= 1:
    print("baby")
elif age > 1 and age <=5:
    print("toddler")
elif age > 5 and age <=12:
    print("child")
elif age > 13 and age <= 19:
    print("teenage")
elif age > 20 and age <= 34:
    print("adult")
elif age >= 60:
    print("old codger")
else:
    print("Younger")


# In[23]:


#25 Take two number a,b from the user and check whether a is divisible by b or not 
a=int(input())
b=int(input())
if b!=0:
    if ((a%b==0)):
        print("a is divisible by b")
    else:
        print("a is not divisible by b")
else:
    print("Zero division error")


# In[29]:


#26Take a letter from the user and print that letter belongs to which category
#I.e is it a small letter or capital letter or number or special symbol 
s=input("enter one letter\n")
if s.isdigit():
    print("it is a number")
elif s.islower():
    print("it is a small letter")
elif s.isupper():
    print("it is a capital letter")
else:
    print("it is a Special symbol")


# In[6]:


#25 looping statements take a number from the user and check whether it is prime? 
n=int(input())
factors=0
for i in range(2,n):
    if (n%i==0):
        factors=factors+1
if factors==0 and (n!=1 and n!=0):
    print("prime")
else:
    print("not prime")
    


# In[10]:


#26.take a string from the user and check contains only digits or not? 
a=input()
if a.isdigit():
    print("true")
else:
    print("False")


# In[15]:


#27take a string from the user and check contains only  alphabets or not? 
a=input()
b=""
for i in a:
    if ((i>="a" or i>="A") and (i<="z" or i>="Z")):
        b=b+i
if len(a)==len(b):
    print("True")
else:
    print("False")


# In[26]:


#28 take a string from the user and check contains only  special chars or not? 
a=input()
c=0
for i in a:
    if not i.isalnum():
        c=c+1 
if c==len(a):
    print("True")
else:
    print("False")


# In[30]:


#29.Take a string from the user and check contains only capital letters or not?
a=input()
b=0
for i in a:
    if i.isupper():
        b=b+1
if b==len(a):
    print("True")
else:
    print("False")


# In[32]:


# 30.Take a string from the user and check contains only small letters or not?
a=input()
b=0
for i in a:
    if i.islower():
        b=b+1 
if b==len(a):
    print("True")
else:
    print("False")


# In[7]:


'''
31. WAP to replace last n occurrence of give string.
For example:”apple,orange,apple,grape,orange,apple,apple,orange”
source: “apple”
last occurrences: 2
replace with: APPLE
output:”apple,orange,apple,grape,orange,APPLE,APPLE,orange”
'''
a=input()
b=input()
c=int(input())
d=input()
e=a.rsplit(b,c)
f=d.join(e)
print(f)



# In[13]:


#32 WAP to check given string contains numbers or not. it should consider float numbers also.
a=input()
c=0
if a.isdigit() or a.count("."):
    c=c+1
if c>=1:
    print("True")
else:
    print("False")


# In[25]:


#33   Convert the total string in to lower case. Without using lower() function.
s=input()
b=s.upper()
result=""
for i in b:
    a=int(ord(i))+32
    result=result+chr(a)
print(result)


# In[ ]:


#34   Convert the total string in to upper case. Without using upper() function.
s=input()
b=s.lower()
result=""
for i in b:
    a=int(ord(i))-32
    result=result+chr(a)
print(result)


# In[1]:


'''35Show the below menu to the user until and until user select quit and display corresponding os message
      Menu:

        1. windows
        2. Linux
        3. Mac
        4. quit
'''       
while True:
    a=input("enter below options \n 1.windows \n 2.Linux \n 3.Mac \n 4.quit \n ")
    if a=="1":
        print("windows")
    elif a=="2":
        print("Linux")
    elif a=="3":
        print("Mac")
    if a=="4":
        print("quit")
        break


# In[2]:


#36 Take a string from the user and check contains at least one digit or not?
s=input()
c=0
for i in s:
    if i.isdigit():
        c=c+1
if c>=1:
    print("string contains digit")
else:
    print("string does not contain digit")
    


# In[5]:


#37. take a string from the user and check contains at least one alphabets or not?
a=input()
c=0
for i in a:
    if i.isalpha():
        c=c+1
if c>=1:
    print("string contains alphabets")
else:
    print("String does not contains alphabets")


# In[4]:


#38 take a string from the user and check contains at least one chars or not? 
a=input()
if len(a)==0:
    print("String has no characters")
else:
    print("String has characters")
    


# In[7]:


#39 take a string from the user and check contains at least one capital letter or not? 
a=input()
count=0
for i in a:
    if (i>="A" and i<="Z"):
        count=count+1
if count>=1:
    print("yes the string contains capital letter")
else:
    print("the string does not contain capital letter")


# In[9]:


#40take a string from the user and check contains at least one small letter or not?
a=input()
count=0
for i in a:
    if (i>="a" and i<="z"):
        count=count+1
if count>=1:
    print("yes the string contains small letter")
else:
    print("the string does not contain small letter")


# In[18]:


#41  Print the first 100 odd numbers 
result=""
for i in range(1,200):
    if ((i%2)!=0):
        result=result+str(i)+" "
print(result)        


# In[17]:


#42 Determine the factors of a number entered  by the user 
n=int(input())
for i in range(1,n+1):
    if n%i==0:
        print(i)


# In[35]:


#43 Play a number guessing game (User enters a guess, you print YES or Higher or Lower).
#This should continue until and until user gives a correct number or want to quit in the middle. 
import random
a=random.randint(1,100)
while True:
    n=(input("enter number\n"))
    if n=="q":
        print("the correct answer is:"+str(a))
        break
    elif n==str(a):
        print("you have guess a correct number")
    elif n<str(a):
        print("please enter higher number")
    elif n>str(a):
        print("please enter lower number")


# In[2]:


#44.Take two numbers from the user a,b check whether a is divisible by b or not? 
a=int(input())
b=int(input())
if a%b==0:
    print("a is divisible by b")
else:
    print("a is not divisible by b")
    


# In[3]:


#45.Find the sum of all the multiples of 3 or 5 below 1000 
sum=0
for i in range(1,1000):
    if (i%3==0) or (i%5==0):
        sum=sum+i
print(sum)        


# In[4]:


#46.Write a program to find out big of two numbers 
a=int(input())
b=int(input())
if a>b:
    print(a)
else:
    print(b)


# In[6]:


#47. Write a program to find out biggest number in the given numbers. 
n=list(map(int,input().split()))
print(max(n))


# In[54]:


#48. find out the index of  third occurrence of given substring (apple apple orange guava apple,apple,output 5)
sentence=input().split()
substring=input()
count=0
for i in range(len(sentence)):
    if sentence[i]==substring:
        count=count+1
        if count==3:
            print(i)
            break


# In[23]:


#49.find out the index nth occurrence of given substring 
sentence=input().split()
substring=input()
count=0
for i in range(len(sentence)):
    if sentence[i]==substring:
        count=count+1
        result=i
print(result)        


# In[28]:


#50.Take some single digit numbers from the user and findout min, maximum, sum, average 
n=list(map(int,input().split()))
print(min(n))
print(max(n))
sum=0
for i in n:
    sum=sum+i
print(sum)
print(sum/len(n))


# In[38]:


'''51. print the number in proper mathematical way. 

Consider that we have 6 digit numbers. 

Number format  WAP> 10 -> 000010 

       		100 ->  000100 

      		1000 ->  001000 

 		 2345678  ->  2345678 

If the number has more than 6 digits then print as it is. 
'''
a=input()
b=len(a)
c=6-b
if b==6:
    print(a)
else:
    d="0"*int(c)
    print(d+str(a))
    


# In[39]:


#52. names  ="emp1,emp2,emp3,emp4" iterate through the employee names. 
a=input().split(",")
for i in a:
    print(i)
    


# In[ ]:


#53. Take actual string, source string, destination string. 
#replace first nth occurrences of source string with destination string of actual string. 
actual_string=input().split()
source_string=input()
destination_string=input()
count=0
for i in range(len(actual_string)):
    if source_string==actual_string[i]:
        count=count+1
        result=i 
actual_string[result]=destination_string
res=""
for i in actual_string:
    res=res+i+" "
print(res)    


# In[3]:


''' 54. Take a two numbers from the user and do below menu driven operations 

1. addition 

2. multiples 

3.division 

4.sqrt 

5. pow    a**b 

6.subtraction   

After selection do the corresponding operation. 

Note: user may give int, or float numbers. 
You should check whether it is proper digits or not. 
I.e the user given string should be in the position to convert to float. 
Other wise show the “inproper string given” Error. 
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


# In[1]:


#55.Take numbers from the user and find out min, maximum, sum, average 
a=list(map(int,input().split()))
sum=0
print(min(a))
print(max(a))
for i in a:
    sum=sum+i
print(sum)
print(sum/len(a))


# In[8]:


# 56.l=[1,2,3,5,7,8,9,10,11,12,13,20,22,23,24,25,26,27,20,21,22,4] 
# find out how many even numbers are there and how many odd numbers are there and 
# how many positive numbers are there and how many negative numbers are there and 
# how many prime numbers are there and
# how many perfect numbers are there and 
# how many Armstrong numbers are there and 
# how many palindrome numbers are there. 
n=list(map(int,input().split()))
new=[]
news=[]
even=0
odd=0
positive=0
negative=0
count=0
counts=0
for i in n:
    if (i%2==0) and (i>0):
        even=even+1
    if i>0:
        positive=positive+1
    if i<0:
        negative=negative+1 
    if ((i%2)!=0) and (i>0):
        odd=odd+1 
print(f'The no of even numbers are:{even}')
print(f'The no of odd numbers are:{odd}')
print(f'The no of positive numbers are:{positive}')
print(f'The no of negative numbers are:{negative}')
for i in n:
    factors=0
    for j in range(2,i):
        if (i%j==0):
            factors=factors+1 
    if factors==0 and i>0:
        new.append(i)
sum=0        
for i in new:
    sum=sum+1
print(f'The no of prime numbers are:{sum}') 
for i in n:
    perfect=0
    for j in range(1,i):
        if (i%j==0):
            perfect=perfect+j
    news.append(perfect)
for i in range(len(n)):
    if n[i]==news[i]:
        counts=counts+1
print(f'The no of perfect numbers are:{counts}') 
for i in n:
    i=str(i)
    res=0
    a=len(i)
    for j in range(int(a)):
        b=i[j]
        print(b)
        #res=res+b
#print(res)        


# In[11]:


#57.Take a string from the user and find out how many digits are there, 
#how many special symbols are there, how many small letters are there, how many caps are there. 
user=input()
count=0
small=0
caps=0
special_symbols=0
for i in user:
    if i.isdigit():
        count=count+1
    elif (i>="a" and i<="z"):
        small=small+1
    elif (i>="A" and i<="Z"):
        caps=caps+1
    else:
        special_symbols=special_symbols+1 
print(f'The no of digits are: {count}')
print(f'The no of small are: {small}')
print(f'The no of capita_letters are: {caps}')
print(f'The no of special_symbols are: {special_symbols}')


# In[12]:


#58.Take a char from the user and find out how many number of occurrences are there in given string
user=input()
char=input()
count=0
for i in user:
    if i==char:
        count=count+1
print(count)        


# In[15]:


#59.Take a element from the user and find out how many times the  element occurred in given list

#example i have took :The end of the day is not same as the previous day:day:output is 2
user=input().split()
element=input()
count=0
for i in user:
    if i==element:
        count=count+1
print(count)    


# In[17]:


#60.Take an element from the user and find out how many number of occurrences are there in given tuple 
a=input().split()
element=input()
b=tuple(a)
count=0
for i in b:
    if i==element:
        count=count+1
print(count) 


# In[2]:


#61. Reverse the string
#without effecting the special symbols. It involves three variations. Write code for three variations.
#62.Input: abc123,#$45def6%$^789$%^, output: $%^987%$^6fed54,#$321cba 
a="abc123,#$45def6%$^789$%^"


# In[3]:


#63.abc123,#$45def6%$^789$%^, output: 9876fe,#$d54321%$^cba$%^


# In[5]:


#64.Inout: "123,#$456%$^789$%^", Output: 321,#$654%$^987$%^  Only numbers has to reverse. 


# # Functions 

# In[5]:


#65. define a function to take person details name and age are mandatory parameters and height weight are optional parameters. 
#If the user willing to pass any other details(like adhar, cell, pan, passport etc..) 
#regarding him then your function should access those details. 
def user_details(name,age,height=0,weight=0,*args):
    print(name,age,height,weight,args)

user_details("john",20)


# In[ ]:


#65a. rewrite above assignments by functions. Can use string functions to solve the string related assignments 


# In[14]:


# 65b. write a function to check given value is even or not.
def even(n):
    if n%2==0:
        return "it is even"
    return "it is not even"
n=int(input())
result=even(n)
print(result)


# In[21]:


#65c. write a function to check given value is prime or not 
def prime(n):
    factors=0
    for i in range(2,n):
        if n%i==0:
            factors=factors+1
    if factors==0 and n!=1:
        return "prime"
    else:
        return "not prime"
n=int(input())
result=prime(n)
print(result)


# In[24]:


#65d.write a function to check given 2 values are  divisible or not 
def divisible(m,n):
    if m%n==0:
        return "m is divisible by n"
    else:
        return "m is not divisible by n"
m=int(input())
n=int(input())
result=divisible(m,n)
print(result)


# # STRINGS

# In[26]:


#67. take a string from the user and check contains only digits or not? 
user=input()
count=0
for i in user:
    if i.isalpha():
        count=count+1
if count==0:
    print("The string contains only digits")
else:
    print("The string does not contains only digits")
        


# In[29]:


#68. take a string from the user and check contains only  alphabets or not? 
user=input()
count=0
for i in user:
    if i.isdigit():
        count=count+1
if count==0:
    print("The string contains only alphabets")
else:
    print("The string does not contains only alphabets")
        


# In[31]:


#69. take a string from the user and check contains only  special chars or not? 
user=input()
count=0
counts=0
for i in user:
    if i.isdigit():
        count=count+1
    elif i.isalpha():
        counts=counts+1
if count==0 and counts==0:
    print("The string contains only special_characters")
else:
    print("The string does not contains only special_characters ")


# In[34]:


#70.take a string from the user and check contains only  capital letters or not? 
user=input()
a=user.upper()
if user==a:
    print("The string contains only capital letters")
else:
    print("The string does not contains only capital letters")
    


# In[37]:


#71.take a string from the user and check contains only  small letters or not? 
user=input()
a=user.lower()
if user==a:
    print("The string contains only small letters")
else:
    print("The string does not contains only small letters")


# In[38]:


#72.WAP to replace last n occurrence. 
actual_string=input().split()
source_string=input()
destination_string=input()
count=0
for i in range(len(actual_string)):
    if source_string==actual_string[i]:
        count=count+1
        result=i 
actual_string[result]=destination_string
res=""
for i in actual_string:
    res=res+i+" "
print(res)    


# In[6]:


#73. WAP to check given string contains numbers or not. it should consider float numbers also.
user=input()
count=0
for i in user:
    if i.isdigit() or (i.count(".")==1):
        count=count+1
if count>0:
    print("string contains numbers and float numbers")
else:
    print("string does not contains numbers and float numbers")


# In[ ]:


#74. Convert the total string in to lower case. 
#Convert the total string in to upper case. 
user=input()
a=user.lower()
b=user.upper()
print(f'lower_case:{a}')
print(f'upper_case:{b}')


# In[36]:


#75. Convert every word start letter into caps. 
#Some how title not working if it contains numbers and special symbols in the word 
user=input()
count=0
for i in user:
    if (not(i.isalpha())):
        if i==" ":
            continue
        count=count+1   
if count>0:
    print("Title is not working because it contains numbers or special symbols")
else:
    print("Title is working")


# In[11]:


# 76.replace last two occurrences of given source string with destination string 
#preserve the delimiter after split.
actual_string=input().split()
source_string=input()
destination_string=input()
count=0
a=[]
result=""
for i in range(len(actual_string)):
    if actual_string[i]==source_string:
        count=count+1
        a.append(i) 
res1=a[-1]
res2=a[-2]
actual_string[res1]=destination_string 
actual_string[res2]=destination_string
for i in actual_string:
    result=result+i+" "
print(result)
       


# In[31]:


#77.write a program to check given substring is there in actual string or not? (search should be case insensitive) 
actual_string=input()
substring=input()
substring_length=len(substring)
j=0
count=0
for i in actual_string:
    if i==substring[j]:
        j=j+1
        if j==substring_length:
            break
if j==substring_length:            
    print("yes given substring is there in actual string ")
else:
    print("yes given substring is not there in actual string ")
        
    


# In[ ]:


#78.example: act="python is a pure object oriented programing language" 
#check whether “pure” is there in act or not. 
#Note: Use in operator 
actual_string=input()
substring=input()
substring_length=len(substring)
j=0
count=0
for i in actual_string:
    if i==substring[j]:
        j=j+1
        if j==substring_length:
            break
if j==substring_length:            
    print("yes given substring is there in actual string ")
else:
    print("yes given substring is not there in actual string ")


# # Data Structures

# In[69]:


#79.l=[10,20,30,[40,50,60],70,[80,90,20]].Convert this list as single dimensional list 
l = [10, 20, 30, [40, 50, 60], 70, [80, 90, 20]]
result=[]
for i in l:
    if type(i)==int:
        result.append(i)
    else:
        result.extend(i)
print(result)        
 


# In[1]:


#80.input: "Google" print count of each character
a=input()
b=set(a)
for i in b:
    c=a.count(i)
    print(i,"=",c)


# In[4]:


#81.Convert n dimensional list to single dimensional list. 
l=input().split()
result=[]
for i in l:
    if type(i)==int:
        result.append(i)
    else:
        result.extend(i)
print(result)


# In[6]:


#82. l=[1,2,3] just make it as a string.
l=[1,2,3]
result=""
for i in l:
    result=result+str(i)+" "
print(result)    


# In[7]:


#83.l=[1,2,3,[4,5,6],7,[8,9,10]] for single dimensional list
l=[1,2,3,[4,5,6],7,[8,9,10]]
result=[]
for i in l:
    if type(i)==int:
        result.append(i)
    else:
        result.extend(i)
print(result)        


# In[8]:


#84.l=['a','A','b','B','d','D','c','C'] WAP to find out case insensitive count and 
l=['a','A','b','B','d','D','c','C'] 
b=set(l)
for i in b:
    d=l.count(i)
    print(str(i)+" "+str(d))


# In[10]:


#85.case insensitive search for an element. 
sentence=input().split()
search_string=input()
if search_string in sentence:
    print("True")
else:
    print("False")


# In[11]:


#86. l=['a','A','b','B','d','D','c','C']  sort the list properly 
l=['a','A','b','B','d','D','c','C']
l.sort()
print(l)


# In[13]:


#87.find the start position of the largest block of repeated characters in a given string
# a=input()
# b=list(a)
# c=set(b)
# res=[]
# for i in c:
#     d=a.count(i)
#     res.append(d)
#     e=max(res)


# In[17]:


#88.WAP to find union and intersection of lists. 
# a=input().split()
# b=input().split()


# In[18]:


#89.input: fun(5) output: [1,2,3,4,3,2,1] 


# In[19]:


#90.input fun('abc') output: [[],][a],[b],[c],[a,b],[b,c],[c,a],[a,b,c]] 


# In[22]:


#91.Remove duplicates from the list: a=[1,2,3,2,3,4,1,,3,4] 
a=input().split()
b=set(a)
c=list(b)
c.sort()
print(c)


# In[23]:


#92. l=['1','2','3'] get the sum of the list 
a=list(map(int,input().split()))
sum=0
for i in a:
    sum=sum+i
print(sum)    


# In[24]:


#93. l1=[1,2,3,4] l2=[5,6,7,8] sum of two lists 
l1=[1,2,3,4]
l2=[5,6,7,8]
res=[]
for i in range(len(l1)):
    sum=l1[i]+l2[i]
    res.append(sum)
print(res)    
    


# In[27]:


#94.Find third max value of element in a list with soring and without sorting a list.
a=input().split()
a.sort()
print(a[-3])


# In[ ]:




