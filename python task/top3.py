from faker import Faker
import random
fake = Faker()
file = open("employees_data.csv", 'w')
file.write("Name,Department,Salary,Mobile\n")
for i in range(100):
    row = f'{fake.name()},{fake.word()},{random.randint(200000, 500000)},{fake.phone_number()}\n'
    file.write(row)
file.close()
print(file)

f = open("employees_data.csv", "r")
f = f.readlines()
#print(f)
sal = []
for i in f[1:]:
    num = 0
    for j in i:
        if j.isdigit():
            num = i.index(j)
            break
    sal.append(int(i[num:num+6]))  
#print(sal)

from faker import Faker
import random
fake = Faker()
file = open("employees_data.csv", 'w')
file.write("Name,Department,Salary,Mobile\n")
for i in range(100):
    row = f'{fake.name()},{fake.word()},{random.randint(200000, 500000)},{fake.phone_number()}\n'
    file.write(row)
file.close()
print(file)