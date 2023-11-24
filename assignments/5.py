'''Take the distance in km 

    	Show that in cm, meters, in milli meters, cents, feets, yards '''
Km = float(input("Enter the input in Km : "))
cm = Km*100000
milli_meters = Km*1e+6
cents = Km*39370.1
feets = Km*3280.84
yards = Km*1093.61
print(cm,milli_meters,cents,feets,yards)
