s = 'apple,orange,mango,grape,apple,grape,apple,banana'
list1 = s.split(',')
count = 0
for i in range(len(list1)-1,-1,-1):
    if list1[i] == 'apple':
        list1[i] = 'APPLE'
        count += 1
    if count == 2:
        break
hello = list1
for i in hello[::-1]:
    if i == 'apple':
        hello.remove('apple')
print(hello)

