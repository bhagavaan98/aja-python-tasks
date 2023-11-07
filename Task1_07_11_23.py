#Task-1 07/11/2023
def details_manadatory(params, manadatory, user_input):
    if sorted(manadatory) == sorted(user_input) :
        
        return 'Manadatory items were given'
    else:

        s1 = list((set(manadatory) - set(user_input)))
        s2 = " ".join(s1)
        diff = []
        for item in user_input:
            if item not in manadatory:
                diff.append(item)       
        dif = " ".join(diff)
        return f'{dif} extra given and {s2} manadatory'

params = ["name", "age", "aadhar", "Phone"]
manadatory = ["name", "age"]
user_input = input("Enter user input separtated by space:- ").split()
#print(user_input)
get = details_manadatory(params, manadatory, user_input)
print(get)