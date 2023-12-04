


##1. Take the input from the user for(Total number of people,Number of seats for bus. Based on two
##inputs Decide how many number of buses required


n=int(input("Enter number of people="))
m=int(input("Enter no of seats are there in a bus="))
if n>=1 and m >=1:
    no_of_buses_required=(n+m-1)//m
    print(no_of_buses_required,"buses are required")
else:
    print("number of people and no of seats for bus must be greater than or equal 1")





##2.take temperature from the user and convert foreign heat -> Celsius.

foreign_heat=float(input("Enter foreign heat temperature="))
celsius=(foreign_heat-32)*5/9
print(celsius,"c")





##3.take temperature from the user and convert Celsius → foreign heat.
celsius=float(input("Enter celsius temperature="))
foreign_heat=(celsius*9/5)+32
print(foreign_heat,"F")





##4.take four number from the user (variables name it as x1,x2,x3,x4)
##Do the below operations
##(x1+x2)**2, (x3+x4)**3
##variance
##standard deviation: sqrt(variance): User math module. Math.sqrt(variance)
##Regression
##y=mx+b
##m=1.23
##b=0.045
##find out y
##y=m*(x1+x2+x3+x4)+b
##Find the average of four numbers
##Find the sum of four numbers
x1=int(input("Enter any number="))
x2=int(input("Enter any number="))
x3=int(input("Enter any number="))
x4=int(input("Enter any number="))
square=(x1+x2)**2
cube=(x3+x4)**3
print("square value is=",square)
print("cube value is=",cube)
print()
m=1.23
b=0.045
x=x1+x2+x3+x4
y=m*x+b
print("The y value is=",y)
print()
print("The average of value of four values is=",x/4)
print("The sum of four values are=",x)





##5.Take the distance in km
##Show that in cm, meters, in milli meters, cents, feets, yards
km=int(input("Enter the distance in km="))
print(f"{km} kilo meters={km*1000} meters")
print(f"{km} kilo meters={km*100000} centi meters")
print(f"{km} kilo meters={km*1000000} milli meters")
print(f"{km} kilo meters={km*3280.84} feets")
print(f"{km} kilo meters={km*1093.61} yards")


# In[58]:


##6.Take the size of your hard disk in GB
##Show that in MB, KB, TB, PB
size=int(input("Enter your hard disk size="))
print(f"{size} GB={size*1024} Mega bytes")
print(f"{size} GB={size*1048576} Kilo bytes")
print(f"{size} GB={size*0.0009765625} Tera bytes")
print(f"{size} GB={size*9.53674316e-7} Peta bytes")


# In[28]:


##7. Take name, age, height from the user and print like below
##The details of the person: Name:name of the person, Age:age of the person, Height:height of the person

##Note: make sure that no space between : and a value and should be space after “COMA”
name=input("Enter your name=")
age=int(input("Enter your age="))
height=float(input("Enter your height="))
print(f"Name:%s,Age:%d,Height:%f"%(name,age,height))





##8. BMI calculation: take required parameters for BMI calculation from the user and calculate BMI of the person.
try:
    weight=float(input("Enter person weight in kilograms="))
    height=float(input("Enter person height in meters="))
    BMI=weight/(height**2)
    print(BMI)
except ValueError:
    print("Invalid input please enter valid input")


##9. name="Jayaram"
##age=1.6
##height=3.5356234
##weight=10.343856783
##By using above inputs print the output
##Name:Jayaram, Age:1.6, Height:3.54, Weight:10.344
##Note: Use format specifiers(%s, %d, %f)
    
name="Jayaram"
age=1.6
height=3.5356234
weight=10.343856783
print("name=%s,age=%f,height=%f,weight=%f"%(name,age,height,weight))
                                


##10. Take three upper case letters from the user convert in to small case.
a=[i.lower() for i in input("Enter 3 characters=") if i.upper()]
print("".join(a))




##11. take base and exponent value from the user and print like in mathematics:
##example: base=2, exponent=3: 2 3
##Use: 2\u00b3
a=int(input("Enter base value="))
b=int(input("Enter exponent value="))

##12. Take some groceries cost prices and print total cost and average cost, what is the max cost, what is the minimum cost.
oil_cost=180
sugar_cost=45
rice_cost=72
salt_cost=20
total_cost=oil_cost+sugar_cost+rice_cost+salt_cost
average_cost=total_cost/4
print("total cost is=",total_cost)
print("average cost is=",average_cost)
print("maximum cost is=",max(oil_cost,sugar_cost,rice_cost,salt_cost))
print("minimum cost is=",min(oil_cost,sugar_cost,rice_cost,salt_cost))


## Variable Assignments:


#13. Assign “ten” value to variable it is 10 otherwise assign “Not ten”
#Note: write two versions of program
#Version1: use and operator
#Version2: use or operator
a=input("Enter value=")
if a=="ten":
    print("It is ten")
else:
    print("It is not a ten")


# # Conditional statements


#13. Take the input from the user for(Total number of people, total number of buses, Number of
#seats for bus, adjust factor). Based on four inputs
#Decide whether there is sufficient buses or not and give solution for how manyextra buses required.

people=int(input("Enter number of people="))
buses=int(input("Enter number of buses="))
seats=int(input("Enter number of seats="))
factor=int(input("Enter adjust factor="))
no_of_buses=(people)//(seats+factor)
print(no_of_buses)
if (people)%(seats+factor)!=0:
    no_of_buses +=1
    if buses>no_of_buses:
        print(f"{no_of_buses} buses required but")
        print(f"{buses-no_of_buses} extra buses are their")
    else:
        print("No sufficient buses")
        print(f"{no_of_buses-buses} buses are required")
else:
    print("sufficient buses")




#14.Take number from the user decide whether it is even or odd.
n=int(input("Enter any number="))
if n%2==0:
    print("{} is a even number".format(n))
else:
    print("{} is an odd number".format(n))


#15.take number from the user decide whether it is positive number or negative number
n=int(input("Enter any number="))
if n>0:
    print("{} is a positive number".format(n))
else:
    print("{} is a negative number".format(n))



#16.take a string from the user print the length. if the user not given anything then show an error message
s=input("Enter any string=")
if len(s)==0:
    print("Error:you did not enter anything")
else:
    print("The length of the string is=",len(s))



#17.code to perform mathematical operations. take two numbers from the user and show the
#below menu
#1. add,
#2. sub,
#3. mul,
#4.div,
#5.quit
#Enter an option:
#based on the option need to perform an operations

a=int(input("Enter any number="))
b=int(input("Enter any number="))
option=input("Enter your option add/sub/mul/div/quit=")
match option:
    case "add":
        print("The addition value is=",a+b)
    case "sub":
        print("The subtraction value is=",a-b)
    case "mul":
        print("The multiplication value is=",a*b)
    case "div":
        print("The division value is=",a/b)
    case "quit":
        print("Thanks for using our application")
    case _:
        print("your option is not correct")



#18. show the menu:
#1. kids
#2. Men's
#3. Women's
#Show the corresponding message based on the selection.

#Option:1: you are a kid
#2: you are a gentlemen
#3: you are a good women

#Mention error message if the option value >3.
option=int(input("Enter any number corresponiding values like 1)kinds 2) men's 3) women's="))
if option==1:
    print("your are a kid")
elif option==2:
    print("your are a gentlemen")
elif option==3:
    print("your are a good women")
else:
    print("we have only 3 options we have to enter 1 or 2 or 3 only")
    



# 19. write a program to chcek given substring is there in actual string or not?
# example: act="python is a pure object oriented programing language"
# check whether “pure” is there in act or not.
# Note: Use in operator

act="python is a pure object oriented programing language"
if "pure" in act:
    print("The given substring is there in actual string")
else:
    print("The given substring is not there in actual string")



#20. Take three numbers from the user and decide which is big
a=int(input("Enter any number="))
b=int(input("Enter any number="))
c=int(input("Enter any number="))
if a>b and a>c:
    print("{} is big".format(a))
elif b>c:
    print("{} is big".format(b))
else:
    print("{} is big".format(c))



# 21. Take age and gender from the user and decide whether he is eligible for marriage in India or not.
# Age criteria: men age > 24, women > 21

def check_eligibility(age,gender):
    if gender=="male":
        return age >24
    elif gender=="female":
        return age>21
    else:
        return False
def main():
    try:
        age=int(input("Enter your age="))
        gender=input("Enter your gender=")
        if check_eligibility(age,gender):
            print(f"{gender} is eligible for marriage")
        else:
            print(f"{gender} is not eligible for marriage")
    except ValueError:
        print("please enter valid age and gender")
main()
    


# 22. Take an age and gender from the user: and mention that what he/she can do in india.
# conditions
# 1. Theatre: 5 for men 7 for women
# 2. Voting system: 18 for men and women
# 3. Marriage in india: 23 for men and for women >21
# 4. For govt jobs: (min:18, max:32) for men and (min:18, max:34) for women
# 5. For driving licence: (min:18, max:60) for men and women
# Eligibility:
# 1. theatre
# 2. Voting system
# 3. Marriage in india
# 4. For govt obs
# 5. For driving licence:

# Enter an option:
# Gender:
# 1. men
# 2. women
# Enter an option:
# Enter an age of person:

def check_eligibility(gender,age):
    if gender=="male":
        theatre_eligibility=age>5
        voting_eligibility=age>=18
        marriage_eligibility=age>23
        government_eligibility=age>=18 and age<=32
        driving_licence=age>=18 and age<=34
    elif gender=="female":
        theatre_eligibility=age>7
        voting_eligibility=age>=18
        marriage_eligibility=age>21
        government_eligibility=age>18 and age<34
        driving_licence=age>18 and age<60
    else:
        print("Invalid gender please enter 'male' or 'female'")
    print(f"1) theatre eligibility={'yes' if theatre_eligibility else 'no'}")
    print(f"2) voting eligibility={'yes' if voting_eligibility else 'no'}")
    print(f"3) marriage eligibility={'yes' if marriage_eligibility else 'no'}")
    print(f"4) government eligibility={'yes' if government_eligibility else 'no'}")
    print(f"5) driving_licence={'yes' if driving_licence else 'no'}")
gender_option=input("Enter gender option 1 for men,2 for women=")
gender="male" if gender_option=="1" else "female"
age=int(input("Enter age="))
check_eligibility(gender,age) 




#23. operating systems:
#1.windows
#2.android
#3.mac
#Enter an option:

#If the user enters 1 then show "Goto first floor and buy windows laptop or mobile"
#If the user enters 2 then show "Goto second floor and buy adroid mobiles"
#If the user enters 3 then show "Goto third floor and buy mac laptop or iphones"
#If the user enters other than 1 or 2 or 3 then show "There is only three floors, please select 1 or
#2 or 3"
option=int(input("Enter your option (1.windows/2.android/3.mac)="))
if option==1:
    print("Goto first floor and buy windows laptop or mobile")
elif option==2:
    print("Goto second floor and buy adroid mobiles")
elif option==3:
    print("Goto third floor and buy mac laptop or iphones")
else:
    print("There is only three floors, please select 1 or 2 or 3")




# 24.Given an age, figure out whether someone's a baby, toddler, child, teenager, adult or old codger.
def age_checking(age):
    if age<0:
        return "Invalid age"
    elif age<1:
        return "Baby"
    elif age<3:
        return "Toddler"
    elif age<13:
        return "Child"
    elif age<20:
        return "Teenager"
    elif age<65:
        return "Adult"
    else:
        return "old codger"
age=int(input("Enter age"))
print(f"The person is a={age_checking(age)}")


#25.Take two number a,b from the user and check whether a is divisible by b or not
a=int(input("Enter any number="))
b=int(input("Enter any number="))
if a%b==0:
    print("a is divisible by b")
else:
    print("a is not divisible by b")



#26. Take a letter from the user and print that letter belongs to which category I.e is it a small letter or
#capital letter or number or special symbol
v=input("Enter any letter=")
if v.islower():
    print("The given value is a small case letter")
elif v.isupper():
    print("The given value is a upper case letter")
elif v.isdigit():
    print("The given value is a digit")
else:
    print("The given value is a symbol")


# # looping statements


#25. take a number from the user and check whether it is prime?
n=int(input("Enter any number="))
if n>1:
    for i in range(2,n//2):
        if n%i==0:
            print("{} is not a prime number".format(n))
            break
    else:
        print("{} is a prime number".format(n))
else:
    print("{} is not a prime number".format(n))
    



#26. take a string from the user and check contains only digits or not?
a=input("Enter anything=")
if a.isdigit():
    print("The given value is a digit")
else:
    print("The given value is not a digit")


#27. take a string from the user and check contains only alphabets or not?
a=input("Enter anything=")
if a.isalpha():
    print("The given value is a alphabet")
else:
    print("The given value is not a alphabet")


# In[27]:


#28. take a string from the user and check contains only special chars or not?
a=input("Enter any special chars=")
if not a.isalnum():
    print("The given value is a special char")
else:
    print("The given value is not a special char")
    


#29.take a string from the user and check contains only capital letters or not?
a=input("Enter any value=")
if a.isupper():
    print("The given value is a capital letter")
else:
    print("The given value is not a capital letter")



#30.take a string from the user and check contains only small letters or not?
a=input("Enter any string=")
if a.islower():
    print("The given string is a small letters")
else:
    print("The given string is not a small letters")


#31. WAP to replace last n occurrence of give string.
#For example:”apple,orange,apple,grape,orange,apple,apple,orange”
#source: “apple”
#last occurrences: 2

#replace with: APPLE
#output:”apple,orange,apple,grape,orange,APPLE,APPLE,orange”
a="apple,orange,apple,grape,orange,apple,apple,orange"
print("APPLE".join(a.rsplit("apple",2)))



#32. WAP to check given string contains numbers or not. it should consider float numbers also.
a=input("Enter any number=")
if a.isalnum():
    print("The given string contain numbers")
else:
    print("The given string does not contain numbers")



#33. Convert the total string in to lower case. Without using lower() function.
a=input("Enter any string=")
if a.isupper():
    for i in a:
        print(chr(ord(i)+32),end="")
else:
    print(a)



#34. Convert the total string in to upper case. Without using upper() function.
a=input("Enter any string=")
if a.islower():
    for i in a:
        print(chr(ord(i)-32),end="")
else:
    print(a)



# 35) Show the below menu to the user until and until user select quit and display corresponding
# os message
# """Menu:
# 1. windows
# 2. Linux
# 3. Mac
# 4. quit
# """

while True:
    option=input("Enter your option 1) windows 2) linux 3) mac 4) quit=")
    if option=="1":
        print("your are selected windows")
    elif option=="2":
        print("your are selected linux")
    elif option=="3":
        print("your are selected mac")
    elif option=="4":
        print("your are selected quit")
        break
    else:
        print("please enter 1 or 2 or 3 or 4")


# 


#36. take a string from the user and check contains at least one digit or not?
a=input("Enter any string=")
if any(i.isdigit() for i in a):
    print("The string contains at least one digit")
else:
    print("The string does not contain at least one digit")





#37. take a string from the user and check contains at least one alphabets or not?
a=input("Enter any string=")
if any(i.isalpha() for i in a):
    print("The string contains at least one alphabet")
else:
    print("The given string does not contain any alphabet")




#38. take a string from the user and check contains at least one chars or not?
a=input("Enter anything=")
if any(not i.isalnum() for i in a):
    print("The given string contains at least one special character")
else:
    print("The given string does not contain any special character")
    





#39. take a string from the user and check contains at least one capital letter or not?
a=input("Enter any string=")
if any(i.isupper() for i in a):
    print("The given string contains atleast one capital letter")
else:
    print("The given string does not contain any capital letter")





#40. take a string from the user and check contains at least one small letter or not?
a=input("Enter any string=")
if any(i.islower() for i in a):
    print("The given string contain at least one small case letter")
else:
    print("The given string does not contain any small case letter")



#41. Print the first 100 odd numbers
count=0
n=1
while count<100:
    if n%2!=0:
        print(n,end=" ")
        count+=1
    n+=1
        


#42. Determine the factors of a number entered by the user
n=int(input("Enter any number="))
fact=1
for i in range(1,n+1):
    fact *=i
print(fact)





# 43. Play a number guessing game (User enters a guess, you print YES or Higher or Lower). This
# should continue until and until user gives a correct number or want to quit in the middle.
# Get a hidden number by using random.randint(1,100)
import random
a=random.randint(1,10)
while True:
    u=input("Enter your guess(for quit enter q)=")
    if u.lower()=="q":
        print("Thanks for quitting")
        break
    try:
        u=int(u)
    except ValueError:
        print("please enter integer values")
        continue
    if a>int(u):
        print("you have entered a smaller number")
    elif a<int(u):
        print("you have entered a bigger number")
    elif a==int(u):
        print("your guess is correct")
        break
    else:
        print("else enter valid inputs")





#45. Find the sum of all the multiples of 3 or 5 below 1000
summ=0
for i in range(1,1000):
    if i%3==0 or i%5==0:
        print(i,end=" ")
        summ+=i
print()
print("The sum of all the multiples of 3 or 5 below 1000 is=",summ)





#46. Write a program to find out big of two numbers
a=int(input("Enter any number="))
b=int(input("Enter any number="))
if a>b:
    print("{} is big".format(a))
else:
    print("{} is big".format(b))




#47. Write a program to find out biggest number in the given numbers.
a=[2,5,6,7,9,1,3,4]
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




#48. find out the index of third occurrence of given substring
a=input("Enter any string=")
n=3
print("{}rd occurance of the string={}".format(n,a[n-1]))



#49. find out the index nth occurrence of given substring
a=input("Enter any string=")
n=int(input("Enter index number="))
print("{} occurance of the string is={}".format(n,a[n-1]))




#50. Take some single digit numbers from the user and findout min, maximum, sum, average
a=20,30,40,10
summ=0
ma=0
mi=a[0]
for i in a:
    summ+=i
    if int(i)>ma:
        ma=i
    if int(i)<mi:
        mi=i
    avg=summ/len(a)
print("The sum of given numbers are=",summ)
print("The maximum number of the given number is=",ma)
print("The minimum number of the given number is=",mi)
print("The average value of the given numbers is=",avg)





51. print the number in proper mathematical way.
Consider that we have 6 digit numbers.
Number format WAP&gt; 10 -&gt; 000010

100 -&gt; 000100
1000 -&gt; 001000
2345678 -&gt; 2345678
If the number has more than 6 digits then print as it is.



# 52. names ="emp1,emp2,emp3,emp4" iterate through the employee names.
a=["emp1","emp2","emp3","emp4"]
for i in a:
    print(i)




#53. Take actual string, source string, destination string. replce first nth occurrences of source
#string with destination string of actual string.
a="hyderabad is the capital of both ap and ts"
print(a.replace("both ap and ts","ts"))



#54. Take a two numbers from the user and do below menu driven operations
#1. addition
#2. multiples
#3.division
#4.sqrt
#5. pow a**b
#6.subtraction
#After selection do the corresponding operation.

#Note: user may give int, or float numbers. You should check whether it is proper digits
#or not. I.e the user given string should be in the position to convert to float. Other wise
#show the “inproper string given” Error.


a,b=[i for i in input("Enter any numbers separated by space=").split()]
try:
    a=int(a)
except ValueError:
    try:
        a=float(a)
    except ValueError:
        print("Invalid input please provide valid input")
try:
    b=int(b)
except ValueError:
    try:
        b=float(b)
    except ValueError:
        print("Invalid input please provide valid input")
option=input("Enter your option add/sub/mul/div/sqrt=")
if option=="add":
    print("The adddition value is=",a+b)
elif option=="sub":
    print("The subtraction value is=",a-b)
elif option=="mul":
    print("The multiplication value is=",a*b)
elif option=="div":
    print("The division value is=",a/b)
elif option=="sqrt":
    print("The square value is=",a**b)
else:
    print("pleaes enter valid option")


#55. Take numbers from the user and find out min, maximum, sum, average
a=[int(i) for i in input("Enter any numbers=").split(",")]
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


# In[28]:


#56. l=[1,2,3,5,7,8,9,10,11,12,13,20,22,23,24,25,26,27,20,21,22,4] find out how many even
#numbers are there and how many odd numbers are there and how many positive numbers are
#there and how many negative numbers are there and how many prime numbers are there and
#how many perfect numbers are there and how many Armstrong numbers are there and how
#many palindrome numbers are there.

a=[1,2,3,5,7,8,9,10,11,12,13,20,22,23,24,25,26,27,20,21,22,4]
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
        even +=1
    else:
        odd +=1
    if i>0:
        positive +=1
    else:
        negative +=1
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


#57. Take a string from the user and find out how many digits are there, how many special
#symbols are there, how many small letters are there, how many caps are there.
a=input("Enter any string that should contain digits,symbols,small case and upper case letters=")
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
    


#58. Take a char from the user and find out how many number of occurrences are there in given string
a=input("Enter any string=")
b=input("Enter any char to find out how many number of occurances are there in given string=")
for i in a:
    c=a.count(b)
print("{} occured {} times".format(b,c))



# 59. Take a element from the user and find out how many times the element occurred in given list
a=["a","b","c","d","e","f","a","g","a","c","d"]
b=input("Enter any element to find out how many times the element occurred in the given list=")
count=0
for i in a:
    if i==b:
        count +=1
print("{} occured {} times".format(b,count))


# In[23]:


#60. Take an element from the user and find out how many number of occurrences are there in given tuple
a=("a","b","c","d","e","f","a","g","a","c","d")
b=input("Enter any element to find out how many number of occurrences are there in a given tuple=")
count=0
for i in a:
    if i==b:
        count +=1
print("{} occured {} times".format(b,count))



##61. Reverse the string without effecting the special symbols. It involves three variations. Write
##code for three variations.


# 62.Input: abc123,#$45def6%$^789$%^, output: $%^987%$^6fed54,#$321cba
s = "abc123,#$45def6%$^789$%^"
sp_ch=""
res=""
num=[i for i in s if i.isalnum()]
for i in s[::-1]:
    if not i.isalnum():
        sp_ch+=i
    else:
        if len(sp_ch)>0:
            res+=sp_ch
            sp_ch=""
        res+=num[-1]
        num.pop(-1)
print(res)



# 63.Input: abc123,#$45def6%$^789$%^, output: 9876fe,#$d54321%$^cba$%^
s="abc123,#$45def6%$^789$%^"
res=""
num=[i for i in s if i.isalnum()]
for i in s:
    if i.isalnum():
        res +=num[-1]
        num.pop(-1)
    else:
        res +=i
print(res)


# 64.Inout: &quot;123,#$456%$^789$%^&quot;, Output: 321,#$654%$^987$%^
s = "123,#$456%$^789$%^"
num=""
result=""
for i in s:
    if i.isdigit():
        num +=i
    else:
        if len(num)>0:
            result +=num[::-1]
            num=""
        result +=i
print(result)


# # FUNCTIONS:


# 65. define a function to take person details name and age are mandatory parameters
# and height weight are optional parameters. If the user willing to pass any other
# details(like adhar, cell, pan, passport etc..) regarding him then your function should
# access those details.

def person_details(name,age,height=None,weight=None,**other_details):
    print("The person name is=",name)
    print("The person age is=",age)
    if height is not None:
        print("The person height is=",height)
    if weight is not None:
        print("The person weight is=",weight)
    if other_details:
        for i,j in other_details.items():
            print(i,"=",j)
person_details("bhagavaan",25)
print()
person_details("ramesh",26,5.5,68)
print()
person_details("eshwar",28,5.3,67,aadhar=123355,cell=98745613)



# 65a. rewrite above assignments by functions. Can use string functions to solve the string
# related assignments
# 65 b. write a function to check given value is even or not
def even(a):
    if a%2==0:
        print("The given value is a even number")
    else:
        print("The given value is not a even number")
n=int(input("Enter any number="))
even(n)




# 65 c. write a function to check given value is prime or not
def prime(n):
    if n>1:
        for i in range(2,n//2):
            if n%i==0:
                print("{} is not a prime number".format(n))
                break
        else:
            print("{} is a prime number".format(n))
    else:
        print("{} is not a prime number".format(n))
a=int(input("Enter any number="))
prime(a)


# In[46]:


# 65 d. write a function to check given 2 values are divisible or not
def check(a,b):
    if a%b==0:
        print("The given two values are divisible")
    else:
        print("The given two values are not divisible")
x=int(input("Enter any number="))
y=int(input("Enter any number="))
check(x,y)


# # STRINGS

# In[48]:


# 67. take a string from the user and check contains only digits or not?
a=input("Enter any string=")
if a.isdigit():
    print("The given string contains only digits")
else:
    print("The given string does not contains only digits")


# In[50]:


# 68. take a string from the user and check contains only alphabets or not?
a=input("Enter any string=")
if all(a.isalpha() for i in a):
    print("The given string contains only alphabets")
else:
    print("The given string does not contain only alphabets")


# In[57]:


# 69. take a string from the user and check contains only special chars or not?
a=input("Enter any string=")
if all(not i.isalnum() for i in a):
    print("The given string contains only special characters")
else:
    print("The given string does not contain only special characters")


# In[59]:


# 70. take a string from the user and check contains only capital letters or not?
a=input("Enter any string=")
if a.isupper():
    print("The given string contains only upper case letters")
else:
    print("The given string does not contains only upper case letters")


# In[2]:


# 71. take a string from the user and check contains only small letters or not?
a=input("Enter any string=")
if a.islower():
    print("The given string contains only small case letters")
else:
    print("The given string does not contain only small case letters")
    


# In[6]:


# 72. WAP to replace last n occurrence.
actual_string=input("Enter actual string=")
source_string=input("Enter source string=")
destination_string=input("Enter destination string=")
row=actual_string[::-1].replace(source_string[::-1],destination_string[::-1],1)
print(row[::-1])


# In[33]:


# 73. WAP to check given string contains numbers or not. it should consider float numbers also.
try:
    a=input("Enter any number=")
    if int(float(a)) or float(a):
        print("The given string contains numbers")
except ValueError:
     print("The given string does not contain numbers and please enter integer or float values")


# In[5]:


# 74. Convert the total string in to lower case.
# Convert the total string in to upper case.
a=input("Enter any string=")
print("converting total string in to lower case=",a.lower())
print("converting total string in to upper case=",a.upper())


# In[36]:


# 75. Convert every word start letter into caps. Some how title not working if it contains numbers
# and special symbols in the word
a=input("Enter any string=")
print(a.title())


# In[37]:


# 76.replace last two occurrences of given source string with destination string preserve the delimiter after split.
a="apple,mango,orange,banana,apple,orange,apple"
print("APPLE".join(a.rsplit("apple",2)))


# In[40]:


# 77. write a program to check given substring is there in actual string or not? (search should be case
# insensitive)
a=input("Enter any string=")
b=input("Enter any substring=")
if b in a:
    print("The given substring is present in the actual string")
else:
    print("The given substring is not present in the actual string")


# In[6]:


# example: act=&quot;python is a pure object oriented programing language&quot;
# 78.check whether “pure” is there in act or not.
# Note: Use in operator
a="python is a pure object oriented programing language"
if "pure" in a:
    print("pure is there")
else:
    print("pure is not there")


# # DATA STRUCTURES

# In[16]:


# 79. l=[10,20,30,[40,50,60],70,[80,90,20]]. Convert this list as single dimensional list
a=[10,20,30,[40,50,60],70,[80,90,20]]
b=[]
for i in a:
    if list != type(i):
        b.append(i)
    else:
        b.extend(i)
print(b)


# In[20]:


# 80. input: "Google" print count of each character
a="Google"
d={}
for i in a:
    d[i]=a.count(i)
for i,j in d.items():
    print(i,"=",j)


# In[22]:


# 81. Convert n dimensional list to single dimensional list.
a=[[1,2],[5,4],[7,8],[9,10]]
b=[]
for i in a:
    for j in i:
        b.append(j)
print(b)


# In[28]:


# 82. l=[1,2,3] just make it as a string.
a=[1,2,3]
b=""
for i in a:
    b +=str(i)
print(b,type(b))


# In[45]:


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


# In[13]:


# 84. l=["a","A","b","B","d","D","c","C"] WAP to find out case insensitive count and 

a=["a","A","b","B","d","D","c","C"]
user=input("Enter value from list=")
c=0
for i in a:
    if i.lower()==user.lower():
        c+=1
print("count=",c)
print()
# 85. case insensitive search for an element.
user=input("Enter value from list=")
for i in a:
    if user.lower()==i:
        print("Have search element in list")
        break


# In[62]:


# 86. l=["a","A","b","B","d","D","c","C"] sort the list properly
a=["a","A","b","B","d","D","c","C"]
print(sorted(a,key=lambda x:(x.lower(),x)))


# In[17]:


# 87. find the start position of the largest block of repeated characters in a given string
s="aaaaaabbbccccc"
set_s=set(s)
item=[]
for i in set_s:
    row=s.count(i)
    item.append((i,row))
ind=max(item,key=lambda a:a[1])
print(ind)
print(s.index(ind[0]))


# In[28]:


# 88. WAP to find union and intersection of lists.
a=[1,2,3,4,5,6]
b=[3,4,5,7,8]
print(list(set(a) | set(b)))
print(list(set(b) & (set(a))))


# In[70]:


# 89. input: fun(5) output: [1,2,3,4,3,2,1]
def fun(a):
    b=[]
    for i in range(1,a):
        b.append(i)
    for i in range(1,a-1)[::-1]:
        b.append(i)
    print(b)
fun(5)
    


# In[90]:


# 90. input fun("abc") output: [[],[a],[b],[c],[a,b],[b,c],[c,a],[a,b,c]]
from itertools import combinations
def fun(a):
    b=[]
    for i in range(len(a)+1):
        b.append(list(combinations("abc",i)))
    c=[]
    for i in b:
        for j in i:
            c.append(list(j))
    print(c)
fun("abc")


# In[8]:


# 91. Remove duplicates from the list: a=[1,2,3,2,3,4,1,3,4]
a=[1,2,3,2,3,4,1,3,4]
b=[]
for i in a:
    if i not in b:
        b.append(i)
print(b)


# In[49]:


# 92. l=["1","2","3"] get the sum of the list
a=["1","2","3"]
b=0
for i in a:
    b +=int(i)
print("The sum of the list is=",b)


# In[31]:


# 93. l1=[1,2,3,4] l2=[5,6,7,8] sum of two lists
a=[1,2,3,4] 
b=[5,6,7,8]
print(a+b)
print()
print(list(map(lambda x,y:x+y,a,b)))


# In[107]:


# 94. Find third max value of element in a list with sorting and without sorting a list.
#without sorting
a=[5,2,3,4,6,7,9,10]
ma=0
for i in range(len(a)-3):
    if a[i]>ma:
        ma=a[i]
print("3rd max value is=",ma)
print()
#with sorting
a=[5,2,3,4,6,7,9,10]
a.sort()
print("3rd max value is=",a[3])


# In[ ]:


# 95. Input = ["1/1","1/2","1/3","1/4","2/5","2/6","2/8"] Output = [["1/1-4"],["2/5-6"],["2/8"]]


# In[1]:


# 96. l=[1,2,3,5,7,8,9,10,11,12,13,20,22,23,24,25,26,27,20,21,22,4] output = [[1, 2, 3], [5], [7, 8, 9,
# 10, 11, 12, 13], [20], [22, 23, 24, 25, 26, 27], [20, 21, 22], [4]]
a=[1,2,3,5,7,8,9,10,11,12,13,20,22,23,24,25,26,27,20,21,22,4]

        
        


# In[52]:


# 97. input = 1,2,3,4,5,6,8,10 output = odd,even,odd,even,odd,even,even,even
a=1,2,3,4,5,6,8,10
for i in a:
    if i%2==0:
        print("even",end=",")
    else:
        print("odd",end=",")


# In[2]:


# 98. input n=3
# output: 
# 111
# 101
# 111
n = 3
for i in range(n):
    if i==0 or i==(n-1):
        print("1"*n)
    else:
        s="1"
        e="1"
        r=n-2
        z="0"*r
        print(s+z+e)
        


# In[53]:


# 99. input: Google
# output: {"g":2,"o":2,"l":1,"e":1} use dictionary comprehension
a="Google".lower()
d={}
for i in a:
    d[i]=a.count(i)
print(d)


# In[98]:


# 100. keys=["k1","k2"], values = ["v1","v2"] form a dictionary.
d={"k1":"v1","k2":"v2"}
print("keys=",list(d.keys()),"values=",list(d.values()))
print()
keys=["k1","k2"]
values=["v1","v2"]
a=dict(zip(keys,values))
print(a)


# In[62]:


# 101. Sort the list marks = [("mohan",80),("satish",90),("purnesh",40),("venkat",30)]
# according to descending order of marks
marks=[("mohan",80),("satish",90),("purnesh",40),("venkat",30)]
m=sorted(marks,key=lambda x:x[1],reverse=True)
print(m)
n=sorted(marks,key=lambda x:x[0],reverse=True)
print(n)


# In[18]:


# 102.write a function to get dynamic list for floating numbers also based on strat and end and
# step parameters
s=1.0
e=13.2
step=1.2
res=[]
while e>s:
    res.append(round(s,2))
    s+=step
print(res)


# In[1]:


# 103. find out all perfect numbers in given range
a=[]
for n in range(1,1000):
    sum=0
    for i in range(1,n):
        if n%i==0:
            sum +=i
    if n==sum:
        a.append(n)
print(a)
    


# In[ ]:


# 104. WAP to do all stack operations using lists


# In[ ]:


# 105.WAP to do all queue operations using lists


# In[2]:


# 106. WAP to remove n occurrences of specified element from a list
a=[2,5,3,4,5,6,2,4,3,5,6,2,3,5,4]
remove=int(input("Enter element to remove="))
count=int(input("Enter occurrences="))
for i in range(count):
    index=a.index(remove)
    a.pop(index)
print(a)


# In[19]:


# 107. compare two lists ignore order. i.e return True l1=[1,2,3,4],l2=[4,2,3,1], fun(l1,l2)->; True
a=[1,2,3,4]
b=[4,2,3,1]
print(sorted(a)==sorted(b))


# In[3]:


# 108. XOR operation in python.
print(True ^ True)


# In[20]:


# 109. how to remove all occurrences of the given element in a list
a=[1,2,5,6,7,8,9]
a.clear()
print(a)


# In[22]:


# 110. how to remove first n occurrences of the given element in a list
a=[8,1,2,3,5,2,6,7,8,2,9,10,11,8,12,2]
remove=int(input("Enter element to remove="))
count=int(input("Enter occurances="))
for i in range(count):
    index=a.index(remove)
    a.pop(index)
print(a)


# In[23]:


# 111. how to remove last n occurrences of the given element in a list
a=[8,1,12,3,5,2,6,7,8,12,9,10,11,8,12,2]
remove=int(input("Enter element to remove="))
count=int(input("Enter occurance="))
a=a[::-1]
for i in range(count):
    index=a.index(remove)
    a.pop(index)
print(a[::-1])


# In[26]:


# 112. how to remove nth occurrences of the given element in a list
a=[1,2,2,3,2,5,6,2,2,3,6,5,6,4,3,5]
n=int(input("Enter element to remove="))
c=int(input("Enter occurrences="))
for i in range(c):
    index=a.index(n)
    a.pop(index)
print(a)


# In[5]:


# 113. WAP to generate list of floats i.e: fun(0,1,0.1), [0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]
def fun(a,b,c):
    res=[]
    while b>a:
        res.append(round(a,2))
        a+=c
    print(res)
fun(0,1,0.1)


# In[6]:


# 114. WAP to remove all occurrences of given substring from actual string
a="Hello,world,Hello,Everyone"
print(a.replace("Hello,",""))


# In[8]:


# 115. WAP to remove first n occurrences of given substring from actual string
a="Hello,world,Hello,python,Hello,world".split(",")
b="Hello"
remove=b
count=int(input("Enter occurrences="))
for i in range(count):
    index=a.index(remove)
    a.pop(index)
print(",".join(a))


# In[9]:


# 116. WAP to remove last n occurrences of given substring from actual string
a="Hello,world,Hello,python,Hello,world".split(",")
b="Hello"
remove=b
a=a[::-1]
count=int(input("Enter occurrences="))
for i in range(count):
    index=a.index(remove)
    a.pop(index)
print(",".join(a[::-1]))


# In[16]:


# 117. WAP to replace last n occurrences of given substring with destination string in actual string
a="Hello world Hello python Hello world"
print("Hi".join(a.rsplit("Hello",2)))


# In[29]:


# 118. WAP to sort the string.
a="bhagavaan"
b="".join(sorted(a))
c="".join(sorted(a,reverse=True))
print("sort the string ascending order=",b)
print("sort the string descending order=",c)


# In[6]:


# 119. take a coma separated numbers and find out max number.
a=1,5,2,6,9,3,7
ma=0
for i in a:
    if i>ma:
        ma=i
print("The maximum value is=",ma)


# In[7]:


# 120. Read a json file. Try to get the information from the file
import json
d={"name":"ramesh","age":25,"salary":15000,"isMarried":True,"isHavingGirlFriend":None}
with open("employee.data","w") as f:
    json.dump(d,f)
    print("to see the data we have to open employee.data file")

with open("employee.data","r") as f:
    result=json.load(f)
print(result)


# In[4]:


# 121.Read a yaml file. Try to get the information from the file
from pyaml import yaml
s={"name":"eshwar","age":15,"grade":"A","IsHavingGirlFriend":None,"isMarried":True}
with open("student.data","w") as f:
    yaml.dump(s,f)
    print("to see the data we have to open the file")

with open("student.data","r") as f:
    result=yaml.safe_load(f)
    print(result)


# In[ ]:


# 122.Read any image data using Opencv


# In[45]:


# 123.make alternative words reversed in given string:
# ex: "python program good language"; "python margorp good egaugnal";
a="python program good language".split()
b=""
for i in range(len(a)):
    if i%2!=0:
        b+=a[i][::-1]+" "
    else:
        b+=a[i]+" "
print(b)
        


# In[36]:


# 124. l=["c","cpp","java","php","python"]
# case insensitive count# l.count("C")->;1
# like count l.own_count("c")->;2 with case insensitive
a=["C","cpp","java","php","python"]
b="".join(a).lower()
print("case insensitive=",b.count("c"))
b="".join(a)
print("case sensitive=",b.count("C"))


# # STRINGS

# In[55]:


# Take two inputs from the user: your program should check for below scenarios.
# 10,20: 30
# 12.34,45.67: 58.01
# +12,-12: 0
# qwe,23we: Enter digits or float values only
a=input("Enter any number=")
b=input("Enter any number=")
try:
    a=int(a)
except ValueError:
    try:
        a=float(a)
    except ValueError:
        print("Please enter digits or float values only")
try:
    b=int(b)
except ValueError:
    try:
        b=float(b)
    except ValueError:
        print("Please enter digits or float values only")
print("{},{}={}".format(a,b,a+b))


# In[14]:


# 116. take the number of employees count from the user and ask the inputs required for the bmi for each
# and every person. The result should be like below
# empid:{“weight:”,”height”:,”age”:,”bmi”:0.9,”result”:”+ve”}
def employee_data():
    try:
        no_of_employees=int(input("Enter no of employees="))
        employee_data={}
        for i in range(no_of_employees):
            eid=int(input("Enter employee id="))
            eweight=float(input("Enter employee weight="))
            eheight=float(input("Enter employee height="))
            age=int(input("Enter employee age="))
            bmi=eweight/(eheight**2)
            result="+ve" if 18.5 <= bmi <=24.9 else "-ve"
            emp_data={"weight":eweight,"height":eheight,"age":age,"bmi":bmi,"result":result}
            employee_data[eid]=emp_data
        print(employee_data)
    except ValueError:
        print("please provide integer values")
employee_data()
        


# # Modules:

# In[ ]:


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


# # FILES

# In[53]:


# 118. copy 1 file content in to another file(Take the source and destination file path from the user)
with open("emp.data","r") as f1:
    data=f1.read()
with open("salary.data","w") as f2:
    f2.write(data)
    print("completed")


# In[50]:


#120. print number of lines, words, characters from the given file
import os
fname=input("Enter file name=")
if os.path.isfile(fname):
    print("file exists=",fname)
    with open(fname,"r") as f:
        lcount=wcount=ccount=0
        for i in f:
            lcount +=1
            no_words_present_in_current_line=len(i.split())
            wcount +=no_words_present_in_current_line
            ccount +=len(i)
        print("no of lines are present in file=",lcount)
        print("no of words are present in the file=",wcount)
        print("no of characters are present in the file=",ccount)
else:
    print("file does not exists=",fname)


# In[15]:


# 121. convert .txt file in .json
import json
with open("employee.data","r") as f:
    data=[json.loads(i) for i in f]
print("the data is=",data)


# In[ ]:


122. Take three columns disease, symptoms, advice in a file and fill the details
Ask the user to enter symptoms. Based on this symptoms Suggest the user to what
disease it may be and few advices.


# In[ ]:


123. Take employees info (id,name, age, adress, sal, height, weight)
a. Take id, provide employee information for that id.
b. find out average salary.
c. find out which age, address taking the heighest salary
d. find out every employee BMI value
e. Finally find out the Organization overall BMI



# In[ ]:


124. read the file which contains the size greater than your ram size


# In[ ]:


125. Read ten gb movie


# In[ ]:


126. Collect emp information in a file Provide these operations.
Menu:
1. Get information of an employee
2. Modify employee information
3. delete an employee information (Only status field change in the employee file)
4. Add an employee.


# In[ ]:


127. Take Source and destination file paths from command line arguments and copy the
sourcontent into destination.
Make Sure that your program checking the below conditions.
1.if the source file not there. Should ask the user to enter new source file or want to quit
a program
2.if the destination file already there in the specified path. Should warn the user want to
proceed or want to enter new destination file name or want to quit



# In[ ]:


128. Bulk file copy.
Take source and destination file paths from a file and copy the source file content into
destination file.
Maintain configuration file and put the below fields there
Source not found: Skip the copy
destination found: skip/replace
maintain a remarks log. What are the files skiped from copy because no source file
found. What are the files skip/replaced because of destination file foun in the specified path
