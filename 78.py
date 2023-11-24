'''replace last two occurrences of given source string with destination string 
 preserve the delimiter after split.'''
source_string = input("Enter the string here : ")
replace_string = input("Enter the string here : ")
destination_string = input("Enter the string here : ")
new_string = source_string[::-1].replace(replace_string[::-1],destination_string[::-1],2)
print(new_string[::-1])