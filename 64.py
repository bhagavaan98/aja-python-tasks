'''Reverse the string.> 
 without effecting the special symbols. It involves three variations. 
 Write code for three variations.'''
s = list("abc123,#$45def6%$^789$%^")
list1=[]
spl = []
for i in s[::-1]:
    if i.isalnum():
        list1.append(i)
    else:
        if not i.isalnum():
            x = s.index(i)
            spl.append(x)
            continue
        for i in spl:
            list1.append(s[i])
            spl.clear()
print(spl)
print(list1)

