#!/usr/bin/env python
# coding: utf-8

# In[8]:


##13
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


# In[8]:


#13 conditional statements
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


#14
a=int(input())
if a%2==0:
    print("Even")
else:
    print("Odd")


# In[ ]:


#15
a=int(input())
if a>=0:
    print("positive")
else:
    print("Negative")


# In[ ]:


#16
a=input()
if a!="":
    print(len(a))
else:
    print("Error message")


# In[10]:


#17
a=int(input())
b=int(input())
c=int(input("enter an option for add=1,sub=2,mul=3,div=4,quit=5"))
if c==1:
    print(a+b)
if c==2:    
    print(abs(a-b))
if c==3:
    print(a*b)
if c==4:
    print(a/b)
if c==5:
    print("quit")
    


# In[3]:


#18
print("enter below options\n 1.kids\n 2.Men's\n 3.women's")
a=int(input())
if a==1:
    print("you are a kid")
if a==2:
    print("you are a gentlemen")
if a==3:
    print("you are a good women")


# In[ ]:


#19
a=input()
b=input()
if b in a:
    print("string is there")
else:
    print("string is not there")


# In[4]:


#20
a=int(input())
b=int(input())
c=int(input())
if a>b and a>c:
    print(a)
if b>a and b>c:
    print(b)
if c>a and c>b:
    print(c)


# In[ ]:





# In[ ]:





# In[5]:


#21
age=int(input())
gender=input()
if (gender=="men" and age>24) or (gender=="women" and age>21):
    print("eligible for marriage")
else:
    print("not eligible for marriage")


# In[11]:


#22
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


#23
user=int(input("enter below options \n 1.windows\n 2.android \n 3.mac \n"))
if user==1:
    print("Goto first floor and buy windows laptop or mobile")
if user==2:
    print("Goto second floor and buy android mobiles")
if user==3:
    print("Goto third floor and buy mac laptop or iphones")
if user>3:
    print("There is only three floors,please select 1 or 2 or 3")


# In[14]:


#24
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


#25
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


#26
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


#25 looping statements
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


#26
a=input()
if a.isdigit():
    print("true")
else:
    print("False")


# In[15]:


#27
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


#28
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


# In[ ]:


#36 Take a string from the user and check contains at least one digit or not?
s=input()
for i in s:
    


# In[ ]:





# In[ ]:





# In[ ]:




