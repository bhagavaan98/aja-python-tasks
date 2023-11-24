'''find out the index of  third occurrence of given substring '''
sen = list(input("Enter the string here : ").split(","))
occ = input("Enter your substring here : ")
count = 0
for i in range(len(sen)-1):
    if sen[i] == occ:
        count+=1
    if count == 3:
        print(i)
        break

