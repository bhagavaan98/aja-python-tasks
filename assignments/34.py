'''WAP to replace last n occurrence of give string. 
For example:”apple,orange,apple,grape,orange,apple,apple,orange” 
source: “apple” 
last occurrences: 2 
replace with: APPLE 
output:”apple,orange,apple,grape,orange,APPLE,APPLE,orange” '''
s = input("Enter your string here : ")
list1 = s.split(',')
count = 0
for i in range(len(list1)-1,-1,-1):
    if list1[i] == 'apple':
        list1[i] = 'APPLE'
        count += 1
    if count == 2:
        break
print(list1)

    


    
    
