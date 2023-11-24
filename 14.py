'''Take the input from the user for(Total number of people, total number of buses, Number of seats for bus, adjust factor). Based on four inputs 

Decide whether there is sufficient buses or not and give solution for how many extra buses required. '''
from math import ceil
people = int(input("Enter the Number of People : "))
Seats = int(input("Enter the Number of seats per Bus : "))
Buses = int(input("Enter the Number of buses : "))
adjust_factor = int(input("Enter the adjust factor : "))

total_seats = Seats*Buses
if people > total_seats:
    extra_people = people - total_seats
    if extra_people > adjust_factor:
        print("Insufficent Buses")
        print(f"The number of extra buses required are {ceil(extra_people/Seats)}")
else:
    print("sufficient buses")
