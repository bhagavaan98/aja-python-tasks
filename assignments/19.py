'''show the menu: 
1. kids 
2. Men's 
3. Women's 
Show the corresponding message based on the selection. 
Option:1: you are a kid 
    2: you are a gentlemen 
    3: you are a good women 
 Mention error message if the option value >3. '''
Option = int(input("Select anyone from the menu or list : \n1.Kid's\n2.Men's\n3.Women's\n"))
if Option == 1:
    print("you are a kid")
elif Option == 2:
    print("you are a gentlemen")
elif Option == 3:
    print("you are a good women")
else:
    print("Error : You should only select from Given Options")