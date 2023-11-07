l = ['a', 'b', 'c', 'a', 'b', 'a', 'c', 'a', 'b']
t = input('enter a target charcter to change last 2 occurences: ')
c = l.count(t)
op = []
print(c
     )
for i in l:
    if i==t and (c!=2 or c!=1):
        c -= 1
    elif c==2 or c==1:
        op += t.upper()
    else:
        op += i
print(op)
