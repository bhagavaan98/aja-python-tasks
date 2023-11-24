'''take temperature from the user and convert foreign heat -> Celsius.'''
Temp = float(input("Please enter the temperature in fahrenheit : "))
Celsius = (5*Temp - 160)/9
print(Celsius)