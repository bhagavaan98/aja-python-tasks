'''write a program to check given substring is there in actual string or not? (search should be case insensitive) 
example: act="python is a pure object oriented programing language" '''
string = input("enter the string here : ").lower()
sub_string = input("enter the substring here : ").lower()
if sub_string in string:
    print("Yes it's present in the string")
else:
    print("No, it's not present in the string ")

