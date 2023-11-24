'''Take a char from the user and find out how many number of occurrences are there in given string '''
String = input("Enter the numbers here : ")
count = 0
char = input("Enter the char here : ")
for i in String:
    if i == char:
        count += 1
print(count)