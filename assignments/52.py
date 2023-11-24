'''find out the index nth occurrence of given substring'''
sen = list(input("Enter the string here : ").split(","))
occ = input("Enter your substring here : ")
occur = int(input("Enter your at what occurance you need the index : "))
count = 0
for i in range(len(sen)-1):
    if sen[i] == occ:
        count+=1
    if count == occur:
        print(i)
        break

