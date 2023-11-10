def name_checking(name):
    k = 0
    for i in name:
        if i.isdigit():
            k = k + 1 
    
    return k > 0
   

def age_checking(y):
    return len(y) in [1,2] and y.isnumeric()

def aadhar_verification(parameters,mandatory,user_input):
    
    if len(user_input) == 2 :
        name = user_input[0]
        age = user_input[1]
        name_validation = name_checking(name)
        age_validation = age_checking(age)
        if name_validation == False and age_validation:
            return "Greetings..! welcome to Aadhar portal"
        elif name_validation == True:
            return "Name is Mandatory"
        elif name_validation == True and age_validation == False:
            if age[len(age)-10:] == "@gmail.com":
                return "Email is extra age is Mandatory"
            else :
               return "Age is Mandatory"
            
            
        
        elif age_validation == False:
            if age[len(age)-10:] == "@gmail.com":
                return "Email is extra age is Mandatory"
            else :
               return "Age is Mandatory"
            
    else :
        return "Aadhar is extra"


parameters = ["name","age","aadhar","phone"]
mandatory = ["name","age"]

#given ["name","aadhar"] ------ age is mandatory
user_input = input().split()

result = aadhar_verification(parameters,mandatory,user_input)
print(result)
