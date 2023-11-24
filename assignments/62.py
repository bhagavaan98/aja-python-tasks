'''Take a element from the user and find out how many times the  element occurred in given list '''
list1 = list(input("Enter the elements here : ").split(","))
element = input("Enter the element which needs to be searched : ")
count = 0
for i in list1:
    if i == element:
        count += 1
print(count)