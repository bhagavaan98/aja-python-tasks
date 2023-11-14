f = open("employees_data.csv", "r")
f = f.readlines()
salary = []
for i in f[1:]:
    num = 0
    for j in i:
        if j.isdigit():
            num = i.index(j)
            break
    salary.append(int(i[num:num+6]))  

sal_length = len(salary)
sum = 0
for s in salary:
    sum += s
avg_sal = sum/sal_length
avg_sal_gr = []
for s in salary:
    if avg_sal > s:
        avg_sal_gr.append(s)
avg_sal_gr.sort()        

c = -1
print("The Top 3 Persons who got salary above average salary of all\n")
print(f[0])
for person in f:
    if str(avg_sal_gr[c]) in person:
        print(person)
        c -= 1