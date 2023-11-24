'''l=[10,20,30,[40,50,60],70,[80,90,20]]. 
Convert this list as single dimensional list '''
l=[10,20,30,[40,50,60],70,[80,90,20]]
s =[]
for i in l:
    if type(i) == int:
        s.append(i)
    else:
        s.extend(i)
print(s)
