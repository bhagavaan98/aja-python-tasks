'''l=['a','A','b','B','d','D','c','C'] WAP to find out case insensitive count and  '''
l=['a','A','b','B','d','D','c','C']
x =[]
for i in l:
    x.append(i.lower())
y = set(x)
for i in x:
    print(f"The count of {i} =",x.count(i))