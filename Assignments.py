#!/usr/bin/env python
# coding: utf-8

# In[1]:


#  1. Take the input from the user for(Total number of people,Number of seats for bus. Based on two inputs
# Decide how many number of buses required

import math

peoples = int(input("Enter no of people..."))
seats  = int(input("Total seats in bus.."))

if peoples > 0 and seats > 0:
    if peoples > seats:
        buses = math.ceil(peoples/seats)
    elif seats > peoples:
        buses = 1
else:
    buses = 'Something went wrong'
print('required buses',buses)



# In[2]:


# 2.take temperature from the user and convert foreign heat -> Celsius.
F = int(input("enter temp in foreignheit.."))
celcius_temp = (F-32) *( 5/9 )
print(f'{celcius_temp:.2f} C')


# In[3]:


#  3.take temperature from the user and convert Celsius → foreign heat.
C = int(input("enter temp in celcius.."))
foreignheit_temp = (C *(9/5))+32
print(f'{foreignheit_temp:.2f} F')


# In[4]:


#    5.Take the distance in km
#     	Show that in cm, meters, in milli meters, cents, feets, yards

km = int(input("Enter distance in km..."))
cm = km/100000
m = km/1000
mm = km/1000000
print(cm)





# In[5]:


# 6.Take the size of your hard disk in GB
#      	Show that in MB, KB, TB, PB
gb = int(input("Enter size of your hard disk in GB..."))

mb = gb*1000
kb = gb*1000000
tb = gb/1000
pb = gb/1000000

print('hard disk in mb',mb)
print('hard disk in kb',kb)
print('hard disk in tb',tb)
print('hard disk in pb',pb)


# In[6]:


#    7.  Take name, age, height from the user and print like below
# The details of the person: Name:name of the person, Age:age of the person, Height:height of the person

name = input("Enter name...")
age = int(input("Enter age..."))
height = int(input("Enter height..."))
print(f"Name:{name}, Age:{age}, Height:{height}ft")


# In[ ]:


'''
4.take four number from the user (variables name it as x1,x2,x3,x4)
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

x1 = int(input("Enter x1..."))
x2 = int(input("Enter x2..."))
x3 = int(input("Enter x3..."))
x4 = int(input("Enter x4..."))

suare = (x1+x2)**2
cube =  (x3+x4)**3
print("Square :",suare)
print("Cube :",cube)

# varience:
mean = x1+x2+x3+x4 / 4
x1_deviation = (x1 - mean)**2
x2_deviation = (x2 - mean)**2
x3_deviation = (x3 - mean)**2
x4_deviation = (x4 - mean)**2
varience = (x1_deviation + x2_deviation + x3_deviation + x4_deviation)/4
print('Varience :',varience)

# standard deviation:
print("Standard deviation:",math.sqrt(varience))

# Regression:
m=1.23
b=0.045
y=m*(x1+x2+x3+x4)+b
print("Regression :", y)

#average:
print('Avearge :',mean)

#sum:
print("sum :",x1+x2+x3+x4)


# In[ ]:


# 8. BMI calculation: take required parameters for BMI calculation from the user and calculate BMI of the person.


# In[ ]:


'''9. name="Jayaram"
age=1.6
height=3.5356234
weight=10.343856783
By using above inputs print the output
Name:Jayaram, Age:1.6, Height:3.54, Weight:10.344
Note: Use format specifiers(%s, %d, %f)
'''
name = input("Enter name...")
age = int(input("Enter age..."))
height = float(input("Enter height..."))
weight = float(input("Enter weight..."))

op = "Name: {}, Age: {:.1f}, Height: {:.2f}, Weight: {:.3f}".format(name, age, height, weight)
print(op)


# In[15]:


# 10. Take three upper case letters from the user convert in to small case.

st = 'AMB'
print(st.casefold())


# In[16]:


# 11. take base and exponent value from the user and print like in mathematics:
#   example: base=2, exponent=3: 23
# Use: 2\u00b3
base = int(input("Enter the base: "))
exponent = int(input("Enter the exponent: "))
result = f"{base}\u00b3"
print(result)


# In[ ]:


def enter_value():
    user_input = input("Enter an integer value: ")    
    if user_input == '':
        return enter_value()
    else:
        value = int(user_input)
        return value
    
dt = enter_value()
print("User entered:",dt ,type(dt))


# # looping statements

# In[19]:


# 25. take a number from the user and check whether it is prime?
num = int(input('Enter num..'))
for i in range(2,num):
    if num%i == 0:
        print(num,'is not prime)
        break
else:
    print(num,'is prime')


# In[ ]:


'''31. WAP to replace last n occurrence of give string.
For example:”apple,orange,apple,grape,orange,apple,apple,orange”
source: “apple”
last occurrences: 2
replace with: APPLE
output:”apple,orange,apple,grape,orange,APPLE,APPLE,orange”
'''

ip = 'apple,orange,apple,grape,orange,apple,apple,orange'
tag = 'apple'
n=2
count = 0
ls = ip.split(",")
print(ls)
for i in range(len(ls)-1,-1,-1):
    if count<2:
        if ls[i] == tag:
            ls[i] = 'APPLE'
            count = count+1     
    else:
        break
print(ls)


# In[ ]:


# 32. WAP to check given string contains numbers or not. it should consider float numbers also.
st = 'robo2.0 cwbchjs1'
print(st.isalnum())
for i in range(len(st)):
    if isinstance(st[i],int):
        print(i)
# print(x)


# In[ ]:


print(dir(st))


# In[ ]:


# 33. Convert the total string in to lower case. Without using lower() function.

st = 'Guido Van Rosuum'
op = ''
for i in st:
    if 'A' <= i <= 'Z':
        op += chr(ord(i)+32)
    else:
        op +=i
print(op)
        
 




# In[ ]:


# 34. Convert the total string in to upper case. Without using upper() function

st = 'Guido Van Rosuum'
op = ''
for i in st:
    if 'a' <= i <= 'z':
        op += chr(ord(i)-32)
    else:
        op +=i
print(op)
        
 


# In[ ]:


# 41. Print the first 100 odd numbers

nums = 1
count = 0
while count<100:
    if nums%2 == 0:
        print(nums)
        count+=1
    nums+=1


# In[ ]:


'''
43. Play a number guessing game (User enters a guess, you print YES or Higher or Lower).
This should continue until and until user gives a correct number or want to quit in the middle.
Get a hidden number by using random.randint(1,100)

'''
import random
while True:
    num = int(input('guess number..'))
    guess = random.randint(1,100)
    if num == guess:
        print("YES!! You got it!")
        break
    elif num < guess:
        print('Lower')
    elif num > guess:
        print('Higher')


# In[10]:


# Write a program to find out big of two numbers

ls = [45,7,8,5,56,5555,665,66655,66,5]
for i in range(len(ls)-1):
    for j in range(i+1):
        if ls[i]>ls[j]:
            temp = ls[i]
            ls[i] = ls[j]
            ls[j] = temp
print(ls[:2])


# In[13]:


'''
51. print the number in proper mathematical way.
	Consider that we have 6 digit numbers.
Number format  WAP> 10 -> 000010
       		100 ->  000100
      		1000 ->  001000
 		 2345678  ->  2345678

'''

num = int(input("enter num.."))
print(str(num).zfill(6))


# In[ ]:


'''61. Reverse the string without effecting the special symbols. It involves three variations. Write code for three variations.
          
	
         64.Inout: "123,#$456%$^789$%^", Output: 321,#$654%$^987$%^
		Only numbers has to reverse.
'''


# In[29]:


# 62.Input: abc123,#$45def6%$^789$%^, output: $%^987%$^6fed54,#$321cba
st = "abc123,#$45def6%$^789$%^"
special = '$%^#!&*,'
#    "$%^987%$^6fed54,#$321cba"
op = ""
s = ''
for i in st:
    if i in special:
        s = s+i
    else:
        op = s+op
        s = ''
        op = i+op
op = s+op
print(op)


# In[30]:


# 63.Input: abc123,#$45def6%$^789$%^, output: 9876fe,#$d54321%$^cba$%^
st = "abc123,#$45def6%$^789$%^"

#       9876fe,#$d54321%$^cba$%^

print(st[:len(st)//2])


# ## Data Structures

# In[33]:


# 79. l=[10,20,30,[40,50,60],70,[80,90,20]]. Convert this list as single dimensional list

ls=[10,20,30,[40,50,60],70,[80,90,20]]
ls1 = []

for i in range(len(ls)):
    if isinstance(ls[i],list):
        for j in ls[i]:
            ls1.append(j)
    else:
        ls1.append(ls[i])
print(ls1)


# In[38]:


# 90. input fun('abc') output: [[],][a],[b],[c],[a,b],[b,c],[c,a],[a,b,c]]

def generate_subsets(input_str):
    n = len(input_str)
    result = [[]]

    for char in input_str:
        result += [curr + [char] for curr in result]

    return result
# Example usage:
input_string = 'abc'
result = generate_subsets(input_string) 
print(result)


# In[13]:


"""
96. l=[1,2,3,5,7,8,9,10,11,12,13,20,22,23,24,25,26,27,20,21,22,4] 
output = [[1, 2, 3], [5], [7, 8, 9, 10, 11, 12, 13], [20], [22, 23, 24, 25, 26, 27], [20, 21, 22], [4]]
"""
l=[1,2,3,5,7,8,9,10,11,12,13,20,22,23,24,25,26,27,20,21,22,4] 
new_ls = []
ls = []
for i in range(len(l)):
   if l[i]==l[i-1]+1:
       ls.append(l[i])
   else:
       new_ls.append(ls)
       ls = []
       ls.append(l[i])
new_ls.append(ls)
print(new_ls[1:])
# print(new_ls)
       


# In[29]:


"""
99. input: Google
    output: {'g':2,'o':2,'l':1,'e':1} use dictionary comprehension

"""

ls = 'google'
dic ={k:ls.count(k) for k in set(ls) }
print(dic)


# In[34]:


# 101. Sort the list 
marks = [("mohan", 80), ("satish", 90), ("purnesh", 40), ("venkat", 30)]
# according to descending order of marks

sort_marks = sorted(marks, key = lambda x:x[1], reverse = True)
print(sort_marks)


# In[42]:


# 102.write a function to get dynamic list for floating numbers also based on strat and end and step parameters
def generate_list(start,end,step):
    ls = []
    current = start
    while current <= end:
        ls.append(f'{current:.2f}')
        current +=step
    return ls

print(generate_list(1.0,10.0,0.7))


# In[45]:


# 103. find out all perfect numbers in given range
num = 10000
ls = []
for i in range(1,num+1):
    summ = 0
    for j in range(1,i):
        if i%j == 0:
            summ+=j
    if summ == i:
        ls.append(i)
print(ls)
        


# In[5]:


# 104. WAP to do all stack operations using lists

class Stack:
    def __init__(self):
        self.list_elements = []
    def is_empty(self):
        return len(self.list_elements) == 0
    def push(self,el):
        element = self.list_elements.append(el)
        print(f"{el} element added at the end")
        return element
    def pop(self):
        if not self.is_empty():
            popel = self.list_elements.pop()
            print(f"{popel} element removed")
            return popel
        else:
            print("List is empty")
    def peek(self):
        if not self.is_empty():
            return self.list_elements[-1]
        else:
            print("List is empty")
    def display(self):
        if not self.is_empty():
            for i in reversed(self.list_elements):
                print(i)
            return self.list_elements
        else:
            print("List is empty")
            
            




# In[10]:


stack = Stack()
stack.display()
stack.peek()
stack.push(30)
stack.push(50)
stack.push(60)
stack.pop()
print()
stack.display()
print()
print(stack.peek())


# In[11]:


class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)
        print(f"{item} enqueued to the queue")

    def dequeue(self):
        if not self.is_empty():
            dequeued_item = self.items.pop(0)
            print(f"Dequeued item: {dequeued_item}")
            return dequeued_item
        else:
            print("Queue is empty")

    def front(self):
        if not self.is_empty():
            return self.items[0]
        else:
            return None

    def display(self):
        if not self.is_empty():
            print("Queue elements:")
            for item in self.items:
                print(item)
        else:
            print("Queue is empty.")



queue = Queue()

queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

queue.display()

front_item = queue.front()


queue.dequeue()
queue.dequeue()
queue.dequeue()

queue.display()


# In[24]:


# 106. WAP to remove n occurrences of specified element from a list

ls = [1,5,4,2,1,4,5,1,5,1,6]
newst = ''
ele = 5
n = 4
c= 1
if ls.count(ele)>=n:
    for i in ls:
        if i == ele and c!=n+1:
            c +=1
            ls.remove(i)   

    print(ls)
else:
    print(f"Element not exist {n} times in a list")


# In[25]:


# 108. XOR operation in python.

def xor_operation(a, b):
    result = a ^ b
    return result

num1 = 10
num2 = 5

result = xor_operation(num1, num2)
print(f"{num1} XOR {num2} is {result}")


# In[40]:


# 118. WAP to sort the string.
s = 'helloworld'
st = list(s)
new = ''
for i in range(len(st)):
    for j in range(0,i+1):
        if ord(st[i]) < ord(st[j]):
            temp = st[i]
            st[i] = st[j]
            st[j] = temp
stt = "".join(st)
print(stt)
            


# In[41]:


import pandas


# In[44]:


print(pandas.__file__)


# In[ ]:


'''
125: take total parameters, out of which few are optional and few are mandatory. Take some parameters from the user and 
check whether the user given all the mandatory paramerters or not.
For example: to insert person details
Total parameters: name,age,height,pan,cell,adhar,passport
mandatory: name,cell,adhar
	if the user given: name,adhar,passport then you need to print cell is mandatory parameter
if the user given: name,cell,adhar,passport then you need to print ok 
if the user given: adhar,passport then you need to print cell,name are mandatory parameter
'''


# In[ ]:





# In[ ]:


"""
116. take the number of employees count from the user and ask the inputs required for the bmi for each and every person. 
The result should be like below
empid:{“weight:”,”height”:,”age”:,”bmi”:0.9,”result”:”+ve”}

"""


# In[19]:


def bmivalue(w,h):
    bmi = w/(h**2)
    return bmi

n = int(input("enter the employees count...."))
d = {}
count = 0
while count<n:
#     d = {}
    empid = input("enter emp id:")
    weight = float(input("weight:"))
    height = float(input("height in cm:"))
    age = int(input("age:"))
    bmi = bmivalue(weight,height)
    result = ''
    if 18.5 < bmi < 24.9:
        result = "+ve"
    else :
        result = "-ve"
    d[empid] = {}
    d[empid]["weight"]=weight
    d[empid]["height"]=height
    d[empid]["age"]=age
    
    d[empid]["bmi"]=bmi
    
    d[empid]["result"]=result
    count +=1
print(d)
            


# In[ ]:


"""
118. copy 1 file content in to another file(Take the source and destination file path from the user)
"""


# In[3]:


with open("data.txt", "r") as f:
    data = f.read()
print(data)


# In[4]:


with open("data1.txt", "w") as f1:
    d = f1.write(data)
    print("Done")
    f1.close()


# In[10]:


"""
122. Keep in mind that the exact command can vary depending on your operating system and how Python is installed 
on your machine. If you encounter any issues,
feel free to provide more details about your system, and I can offer more specific guidance.
"""
import csv

def read_health_data(file_path):
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        health_data = [row for row in reader]
    return health_data

def suggest_disease_and_advice(health_data, symptoms):
    for record in health_data:
        if set(symptoms.lower().split()) & set(record['symptoms'].lower().split()):
            return record['disease'], record['advice']
    return "No matching disease found", "Consult a healthcare professional."

def main():
    file_path = 'health.csv'
    health_data = read_health_data(file_path)

    # Take user input for symptoms
    user_symptoms = input("Enter symptoms (comma-separated): ")

    # Suggest disease and advice
    disease, advice = suggest_disease_and_advice(health_data, user_symptoms)

    # Display suggestions
    print(f"\nBased on the symptoms entered, you may have: {disease}")
    print(f"Advice: {advice}")

if __name__ == "__main__":
    main()


# In[49]:


"""
4. create a user defined datatype, and provide functionalities of addition subtraction and multiplication.
Create three instances(obj1,obj2,obj3) and print an output of obj1+obj2+obj3, obj1-obj2-obj3, obj1*obj2*obj3  
"""


class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
    def __add__(self1,self2):
#         return 20+30
#           return self1.name+self2.name, self1.salary+self2.salary
        new_instance = self1.__class__(self1.name+self2.name, self1.salary+self2.salary)
        return new_instance
    def __mul__(self1,self2):
        new_inst = self1.__class__(self1.name+self2.name, self1.salary* self2.salary)
        return new_inst
    
    def __sub__(self1,self2):
        new_inst = self1.__class__(self1.name+self2.name, self2.salary - self1.salary)
        return new_inst
        return 60
    def __iter__(self):
        for i in self.__dict__.values():
            yield i
        
        
ob1 = Employee('eswer', 50000)
ob2 = Employee('bhagavan', 65000)
ob = ob1+ob2
print(ob)
print(ob.name, ob.salary)
print(ob.__dict__.values())
for i in ob:
    print(i)
print(tuple(ob))

ab = ob1*ob2
print(ab)
print(tuple(ab))

sb = ob1-ob2
print(sb)
print(tuple(sb))






# In[53]:


class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    def __add__(self1,self2):
#         return 20+30
#           return self1.name+self2.name, self1.salary+self2.salary
        new_instance = self1.__class__(self1.name+self2.name, self1.salary+self2.salary)
        return new_instance
    def __mul__(self1,self2):
        new_inst = self1.__class__(self1.name+self2.name, self1.salary* self2.salary)
        return new_inst
    
    def __sub__(self1,self2):
        new_inst = self1.__class__(self1.name+self2.name, self2.salary - self1.salary)
        return new_inst
        return 60
    def __iter__(self):
        for i in self.__dict__.values():
            yield i
        
        
ob1 = Employee('eswer', 50000)
ob2 = Employee('bhagavan', 65000)
ob3 = Employee("Govardhan", 78000)
ob = ob1+ob2+ob3
print(ob)
print(ob.name, ob.salary)
print(ob.__dict__.values())
for i in ob:
    print(i)
print(tuple(ob))

ab = ob1*ob2*ob2
print(ab)
print(tuple(ab))

sb = ob1-ob2-ob3
print(sb)
print(tuple(sb))



# In[54]:


dic = {"name":"sharvan", "age":30, 'salary':60000}
print(dic)


# In[56]:


sum(dic.keys())


# In[57]:


type(dic)


# In[83]:


"""
5. addition, subtraction, multiplication operations are not supported by dictionary.
Write a program to provide addition, subtraction, and  multiplication operations to dictionary.
Write your own definition for operations. 
"""

class modify(dict):
    def __init__(self,di):
        self.di = di
        
#     def __add__(self):
#         return 
        
        
d = modify({'a':1,'b':2})
print(d.__dict__.values())
print(d[0]['a'])


# In[80]:


ls = [{'a':1, 'b':2}]
print(ls[0]['a'])


# In[84]:


dic = {'a':1,'b':2}
dic2 = {'c':3,'d':4}
print(dic+dic2)


# In[93]:


class modify:
    def __init__(self,di):
        self.di = di
        
    def __add__(self,self1):
        return self.di.keys()+self1.di.keys()
        
dic = {'a':1,'b':2}
dic2 = {'c':3,'d':4}       
d = modify(dic)
print(d.__dict__.values())
print(d[0])
d1 = modify(dic2)

print(d+d1)


# In[ ]:




