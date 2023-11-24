'''l=[1,2,3,5,7,8,9,10,11,12,13,20,22,23,24,25,26,27,20,21,22,4] 
find out how many even numbers are there and how many odd numbers are there 
and how many positive numbers are there and how many negative numbers are there 
and how many prime numbers are there and how many perfect numbers are there 
and how many Armstrong numbers are there and how many palindrome numbers are there.'''
l=[1,2,3,5,7,8,9,10,11,12,13,20,22,23,24,25,26,27,20,21,22,4]
even_count = 0
odd_count = 0
neg_count = 0
pos_count = 0
prime_count =0
pref_sum = []
sum1 = 0
count_pref = 0
for i in l:
    if i%2 == 0:
        even_count += 1
    else:
        odd_count += 1
print(f"even numbers are{even_count}")
print(f"odd numbers are{odd_count}")

for i in l:
    if i > 0:
        pos_count += 1
    else:
        neg_count += 1
print(f"positive numbers are{pos_count}")
print(f"negative numbers are{neg_count}")

for i in l:
    if i == 1:
        continue
    for j in range(2,i):
        if i%j == 0:
            break
    else:
            prime_count += 1
print(prime_count)

for i in l:
    for j in range(1,i):
        if i%j == 0:
           sum1 += j
    if sum1 == i:
        count_pref += 1
    sum1 = sum1-sum1
print(count_pref)

