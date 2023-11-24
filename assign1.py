#1..Take the input from the user for(Total number of people,Number of seats for bus. Based on two inputs
#Decide how many number of buses required
number_of_people=int(input('enter number of people'))
number_of_seats_per_bus=int(input('enter number of seats'))
total_number_buses_required=number_of_people//number_of_seats_per_bus
if number_of_people%number_of_seats_per_bus:
    
print('total number of buses required is',total_number_buses_required)


  #2.take temperature from the user and convert fahrenheit -> Celsius.
fahrenhiet=float(input('enter fahrenhiet value:'))
celsius=(fahrenhiet - 32) * 5/9
print(celsius)


#3.take temperature from the user and convert Celsius → foreign heat.

celsius=float(input('enter celsius value'))
fahrenhiet= (celsius * 9/5) + 32
print(fahrenhiet)


'''4.Take four number from the user (variables name it as x1,x2,x3,x4)
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


## 5.Take the distance in km
##  	Show that in cm, meters, in milli meters, cents, feets, yards
distance_km = float(input())
print(f" {distance_km}km to cm is {distance_km*100000} cm")
print(f" {distance_km}km to mtrs is {distance_km*1000} mtrs")
print(f" {distance_km}km to mm is {distance_km*1000000} mm")
print(f" {distance_km}km to Cents is {distance_km*39370.1}")
print(f" {distance_km}km to Feets is {distance_km*3280.84}")
print(f" {distance_km}km to Yards is {distance_km*1093.61}")


## 6.Take the size of your hard disk in GB
##   	Show that in MB, KB, TB, PB
disk_size = float(input("Enter size in GB:- "))
print(f' size of {disk_size}Gb to Mb is {disk_size*1000} Mb')
print(f' size of {disk_size}Gb to Kb is {disk_size*1000000} Kb')
print(f' size of {disk_size}Gb to Tb is {disk_size*0.001} Tb')
print(f' size of {disk_size}Gb to Pb is {disk_size/1000000} Pb')


'''
7. Take name, age, height from the user and print like below
The details of the person: Name:name of the person, Age:age of the person, Height:height of the person
Note: make sure that no space between : and a value and should be space after “COMA”
'''
name,age,height = map(str,input().split(","))
print(f'The details of the person: Name:{name}, age:{age}, height:{height}')


##8. BMI calculation: take required parameters for BMI calculation from the user and calculate BMI of the person.
height = float(input("Enter your height:- "))
weight = float(input("Enter your weight:- "))
bmi = weight/(height**2) 
print("The BMI of yours is", bmi)


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
info = "Name: %s, Age: %.1f, Height: %.2f, Weight: %.3f"%(name, age, height, weight)
print(info)


# 10. Take three upper case letters from the user convert in to small case.
letter = input("Enter Three Upper Case Letters:- ")
print(letter.lower())


# 11.Take base and exponent value from the user and print like in mathematics:
# example: base=2, exponent=3: 23
base = input("Enter base value:- ")
exponent = input("Enter exponent value:- ")
exponent = f'{base}^{exponent}'
print(exponent)


# 12. Take some groceries cost prices and print total cost and average cost, what is the max cost, what is the minimum cost.
cost_prices = [58,64,28,4,30]
total_cost = sum(cost_prices)
avg_cost = total_cost / len(cost_prices)
max_cost = max(cost_prices)
min_cost = min(cost_prices)
print("Total cost:-", total_cost)
print("Average cost:-", avg_cost)
print("Max cost:-", max_cost)
print('Min cost:',min_cost)


# 13. Assign “ten” value to variable it is 10 otherwise assign “Not ten”
# Note: write two versions of program
# Version1: use and operator
v1 = int(input("Enter value:- "))
v2 = int(input("enter value:- "))
if v1 and v2:
    print("ten")
else:
    print("Not ten")

#using or
v1 = int(input("Enter value:- "))
v2 = int(input("enter value:- "))
if v1 or v2:
    print("ten")
else:
    print("Not ten")


# 13. Take the input from the user for(Total number of people, total number of buses, Number of seats
#     for bus, adjust factor). Based on four inputs
#     Decide whether there is sufficient buses or not and give solution for how many extra buses required.

people = int(input("Enter number of people:- "))
buses = int(input("Enter number of buses:- "))
seats = int(input("Enter number of seats:- "))
factor = int(input("Enter adjust factor:- "))

#seats_per_bus = seats//buses
no_of_buses = (people+factor)//(seats)
print(no_of_buses)
if (people+factor)%seats != 0:
    no_of_buses += 1
    
    if buses > no_of_buses:
        print(f"{no_of_buses} buses required but")
        print(f"{buses-no_of_buses} extra buses are their")
    else:
        print("No Sufficient buses")
        print(f"{no_of_buses-buses} buses are required")
        
else:
    print("Sufficient buses")
    

    
# 14.Take number from the user decide whether it is even or odd.

value = int(input("Enter a value:- "))
if value%2 == 0:
    print("EVEN")
else:
    print("ODD")


# 15.take number from the user decide whether it is positive number or negative number

num = input('enter a number')
if num[0] == "-":
    print("Negative number")
else:
    print("Positive number")


# 16.take a string from the user print the length. if the user not given anything then show an error message

string = input("Enter a word:- ")
len_string = len(string)
print(len_string) if len_string else "Error"


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
    print("Goto second floor and buy adroid mobiles")
elif user == 3:
    print("Goto third floor and buy mac laptop or iphones")
else:
    print("There is only three floors, please select 1 or 2 or 3")



# 24.Given an age, figure out whether someone's a baby, toddler, child, teenager, adult or old codger.

age = int(input("Enter your age:- "))
if age <= 1:
    print("baby")
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


# 26. Take a letter from the user and print that letter belongs to which category I.e is it a small letter or capital letter
# or number or special symbol

user = input("Enter any character only once:- ")
if user.isupper():
    print("entered value is Upper case")
elif user.islower():
    print("entered value is Lower case")
elif user.isdigit():
    print("entered value is Number")
else:
    print("entered value is Special character")


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


# 26. Take a string from the user and check contains only digits or not?

string = input("Enter input:- ")

if string.isdigit():
    print("Contain only digits")
else:
    print("Does not contain only digits")


# 27. Take a string from the user and check contains only alphabets or not?
string = input("Enter input:- ")

if string.isalpha():
    print("Contains only alphabets")
else:
    print("Does not contains only alphabets")


# 28. Take a string from the user and check contains only special chars or not?
string = input("Enter input:- ")
if all(not i.isalnum() for i in string):
    print("The string contain only special characters")
else:
   print("The string does not contain special characters")

    
# 29.Take a string from the user and check contains only capital letters or not?

string = input("Enter input:- ")

if all(i.isupper() for i in string):
    print("Contains only capital letters")
else:
    print("Does not contan only capital letters")


# 30.Take a string from the user and check contains only small letters or not?

string = input("Enter input:- ")

if all(i.islower() for i in string):
    print("Contains only small letters")
else:
    print("Does not contain only small letters")


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


# 33. Convert the total string in to lower case. Without using lower() function.

string = input("Enter input:- ")
res = ""
for i in string:
    res += chr((ord(i))+32)
print(res)


# 34. Convert the total string in to upper case. Without using upper() function.

string = input("Enter input:- ")
res = ""
for i in string:
    res += chr(ord(i)-32)
print(res)


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


# 36. Take a string from the user and check contains at least one digit or not?

string = input("Enter input:- ")

for i in string:
    if i.isdigit():
        print("String contains one digit")
        break
else:
        print("String does not contains digit")


# 37. Take a string from the user and check contains at least one alphabets or not?

string = input("Enter input:- ")

for i in string:
    if i.isalpha():
        print("String contains one alphabets")
        break
else:
    print("String does not contains atleat one alphabets")
        


# 38. Take a string from the user and check contains at least one chars or not?

string = input("Enter input:- ")

if len(string)>=1:
    print("String contains one char")
else: 
    print("String does not contains chars")


# 39. Take a string from the user and check contains at least one capital letter or not?

string = input("Enter input:- ")

for i in string:
    if i.isupper():
        print("String contains  capital letter")
        break
else:
        print("String does not contains capital letter")
    

# 40. Take a string from the user and check contains at least one small letter or not?

string = input("Enter input:- ")

for i in string:
    if i.islower():
        print("String contains at least one lower letter")
        break
else:
    print("String does not contains at least one lower letter")


# 41. Print the first 100 odd numbers
count = 0
result = ""
num = 1
while 100 > count:
    if num%2 != 0:
        result += str(num)+" "
        count += 1
    num+= 1
        
print(result)      


# 42. Determine the factors of a number entered by the user

user = int(input())
for i in range(1, user+1):
    if user%i == 0:
        print(i)


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


""" WAP to find union and intersection of lists. """ 

# a = [1,2,4,6,7,3]
# b = [10,2,6,4,9,13]

# intersection = []
# union = a 
# for i in b:
#     if i not in union:
#         union.append(i)
    
# print(union)
# for i in a:
#     if i in b:
#         intersection.append(i)
# print(intersection)


""" Remove duplicates from the list: a=[1,2,3,2,3,4,3,4] """ 
a=[1,2,3,2,3,4,3,4]


for i in a[::-1]:
    if a.count(i) > 1 :
        a.remove(i)
print(a)


a=[5,6,3,6,7,8,10,11,10]
l=[]
for i in a:
    if i not in l:
        l.append(i)
print(l)



""" names = "emp1,emp2,emp3,emp4" iterate through the employee names. """

names = "emp1,emp2,emp3,emp4"

for name in names.split(","):
    print(name)


""" 56. l=[1,2,3,5,7,8,9,10,11,12,13,20,22,23,24,25,26,27,20,21,22,4] find out how many even
numbers are there and how many odd numbers are there and how many positive numbers are
there and how many negative numbers are there and how many prime numbers are there and
how many perfect numbers are there and how many Armstrong numbers are there and how
many palindrome numbers are there. """



l=[1,2,3,5,7,8,9,10,11,12,13,20,22,23,24,25,26,27,20,21,22,4]

even = [i for i in l if i % 2 == 0]
odd = [i for i in l if i % 2 != 0]
positive = [i for i in l if i >= 0 ]
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


from random import randint
number = randint(1,100)
while True:
    u = input()
    if u == "q":
        break
    elif u.isalnum():
        if int(u) > number:
            print("My number is :", number, "Your number is: ", u )
        elif int(u) < number:
            print("Smaller")
        elif int(u) == number:
            print("congrats")
        
    

#43. Play a number guessing game (User enters a guess, you print YES or Higher or Lower). 
#This should continue until and until user gives a correct number or want to quit in the middle.

from random import randint
number = randint(1,100)
while True:
    u = input()
    if u == "q":
        break
    elif u.isalnum():
        if int(u) > number:
            print("My number is :", number, "Your number is: ", u )
        elif int(u) < number:
            print("Smaller")
        elif int(u) == number:
            print("congrats")




# """ WAP to find union and intersection of lists. """ 

# a = [1,2,4,6,6,7,7,3]
# b = [10,2,6,4,9,13]

# intersection = []
# union = []
# for i in b:
#     if i not in union:
#         union.append(i)
    
# print(union)
# for i in a:
#     if i in b:
#         intersection.append(i)
# print(intersection)


# l=["1","2","3"] get the sum of the list 
l=["1","2","3"]
c = lambda x : int(x)
print(sum(list(map(c,l))))


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


# 118. WAP to sort the string.
s = "apple"
print("".join(sorted(s)))


# 103. Find out all perfect numbers in given range

def find_perfect(n):
    s = sum(filter(lambda x: n%x == 0, range(1,n)))
    return  s == n




