print("Celsius temperature\tFahrenheit Equivalent")
for currentCelsiusTemperature in range(21):
    fahrenheitTemperatureEquivalent = ( 9 / 5 ) * currentCelsiusTemperature + 32
    print( currentCelsiusTemperature, "\t\t\t\t", format( fahrenheitTemperatureEquivalent, ".1f"))
