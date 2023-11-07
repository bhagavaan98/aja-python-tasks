userinput = list((input('Enter here : ').split()))
mandatory = ['name', 'age']
if mandatory == userinput:
    print(f'{mandatory[0]} and {mandatory[1]} are presnet in the given list')
else:
    if set(mandatory) > set(userinput):
        list1 = list(set(mandatory) - set(userinput))
        print(f'{list1[0] or list1[1]} these are missing')
    elif set(mandatory).issubset(set(userinput)):
        list2 = list(set(userinput)- set(mandatory))
        print(f'{list2} these are extra inputs')
    elif set(userinput) != set(mandatory):
        elements = set(userinput)-set(mandatory)
        if set(elements) == set(mandatory):
            print(f'{set(userinput).difference(set(mandatory))} these are extra')
        else: 
            set(elements) != set(mandatory)
            print(f'{set(userinput).difference(set(mandatory))} these are extra and {(set(mandatory))-(set(mandatory).intersection(set(userinput)))} these are missing')
