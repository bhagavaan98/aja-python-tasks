'''Take an element from the user and find out how many number of occurrences are there in given tuple'''
tup = tuple(input("Enter the elements here : ").split(","))
element = input("Enter the element which needs to be searched : ")
count = 0
for i in tup:
    if i == element:
        count+= 1
print(count)
