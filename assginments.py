""" 1  Take the input from the user for(Total number of people, Number of seats for bus. Based on two inputs 

Decide how many number of buses required """

no_of_people = int(input())
no_of_busses = int(input())
filled_busses = no_of_people // no_of_busses 
if filled_busses == 0:
    print(filled_busses)
else:
    print(filled_busses + 1)