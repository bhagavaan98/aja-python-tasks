from faker import Faker
import random
fake = Faker()
f2 = open("new25.csv","w")
f2.write("Name,Department,Salary\n")
for i in range(150):
    row = f'{fake.name()},{fake.word()},{random.randint(150000, 250000)}\n'
    f2.write(row)
f2.close()

f2 = open("new25.csv","r")  
data = f2.read()
print(data)
f2.close()
