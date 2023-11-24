''' l=[1,2,3,[4,5,6],7,[8,9,10]] for single dimensional list '''
l=[1,2,3,[4,5,6],7,[8,9,10]]
s =[]
for i in l:
    if type(i) == int:
        s.append(i)
    else:
        s.extend(i)
print(s)
