print ("========FAHRENHEIT TO CELSIUS CONVERTER PROGRAM========")
print ("=======================================================")

FahrenH = eval(input("Kindly enter the temperature in Fahreinheit --> :   "))
celsius = ((FahrenH - 32 ) * 5) / 9

print (f" {FahrenH} degrees Fahrenheit converted to celsius is{round(celsius,2)} degrees")
print(round(celsius, 2))