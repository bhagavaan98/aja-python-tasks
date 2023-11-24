'''take a string from the user print the length. if the user not given anything then show an error message'''
Msg = input("Enter the String here : ")
if  Msg:
    print(f"Length of the String is : {len(Msg)}")
else:
    print("Error: Input is not given")