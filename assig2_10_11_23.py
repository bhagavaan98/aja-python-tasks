f = open("new25.csv","r")
f1 = f.readlines()
sal = []
for i in f1[1:-1]:
    sa = i.split(",")
    lens = len(sa)
    for j in range(lens):
        sal.append(int(sa[2]))
        break
print(sal)
avg_sal = int(sum(sal)/len(sal))
print(avg_sal)
unres =[]
for i in sal:
    if i > avg_sal:
        unres.append(i)
print(unres)
unres.sort()
print(unres)
print(unres[-1],unres[-2],unres[-3])