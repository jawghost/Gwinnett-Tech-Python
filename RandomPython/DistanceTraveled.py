vehicleSpeed = float(input("What is the speed of the vehicle: "))
timeTraveled = int(input("How many hours has it traveled?: "))

print()

print( "Hour","\tDistant Traveled" )
for currentHour in range(1, timeTraveled + 1):
    distanceTraveled = vehicleSpeed * currentHour
    print( currentHour, "\t",distanceTraveled)
