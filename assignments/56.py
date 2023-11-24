'''Take actual string, source string, destination string. 
replce first nth occurrences of source string with destination string of actual string.'''
sen = list(input("Enter the string here : ").split(","))
occ = input("Enter which substring to be changed here : ")
replace = input("Enter your replacement here : ")
occurs = int(input("Enter here how many occurances need to change : "))
count = 0
for i in range(len(sen)-1):
    if sen[i] == occ:
        count+=1
        sen[i] = replace
    if count == occurs:
        break
print(sen)