actual_string = input("Enter actual string:- ")

source_string = input("Enter source string:- ")
dest_string = input("Enter destination string:- ")

row = actual_string[::-1].replace(source_string[::-1], dest_string[::-1],2)
print(row[::-1])