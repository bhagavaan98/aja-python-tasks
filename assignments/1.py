'''Take the input from the user for(Total number of people, Number of seats for bus. Based on two inputs 

Decide how many number of buses required '''
from math import ceil

Buses = int(input("Enter the number of seats for bus : "))
People = int(input("Enter the number of people : "))

no_of_buses = ceil(People/Buses)

print(no_of_buses)
