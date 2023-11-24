'''Take a string from the user and find out how many digits are there, 
how many special symbols are there, how many small letters are there, 
how many caps are there. '''
String = input("Enter the numbers here : ")
count_digi = 0
count_sym = 0
count_cap =0
count_saml = 0
for i in String:
    if i.isupper():
        count_cap += 1
        continue
    elif i.islower():
        count_saml += 1
    elif i.isdigit():
        count_digi += 1
    else: 
        count_sym += 1
print(count_digi)
print(count_sym)
print(count_cap)
print(count_saml)
        