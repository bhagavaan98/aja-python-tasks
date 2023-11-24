'''Take an age  and gender from the user: and mention that what he/she can 	do in india. 

""" 
conditions 
1. Theatre: 5 for men 7 for women 
2. Voting system: 18 for men and women 
3. Marriage in india: 23 for men and for women >21 
4. For govt jobs: (min:18, max:32)  for men and (min:18, max:34) for 	women 
5. For driving licence: (min:18, max:60) for men and women 

Eligibility: 
1. theatre 
2.  Voting system 
3.  Marriage in india  
4.  For govt obs 
5. For driving licence: 
Enter an option:

Gender: 
1. men 
2. women 
Enter an option: 
Enter an age of person: '''
Gender = int(input("Select your Gender\n1.Man\n2.Woman\n"))
Age = int(input("Enter your age here : "))
if ((Gender == 1 and Age > 5) and ( Age < 18)) or ((Gender == 2 and Age > 7) and ( Age < 18)):
    print("Eligibility:\n1. theatre")
elif ((Gender == 1 and Age > 18) and ( Age < 23)) or ((Gender == 2 and Age > 18) and ( Age < 21)):
    print("Eligibility:\n1.theatre\n2.Voting system\n3.Marriage in india\n4.For govt obs\n5.For driving licence")
elif ((Gender == 1 and Age > 18) and ( Age < 60)) or ((Gender == 2 and Age > 18) and ( Age < 60)):
    print("Eligibility:\n1.theatre\n2.Voting system\n3.Marriage in india\n4.For govt obs\n5.For driving licence")
else:
    print("Error : Enter age less than 60")