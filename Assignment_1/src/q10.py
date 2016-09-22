celsius = int(input('Enter the temperature in celsius: '))

def getfah(temp):
    print ('Temperature in Fahrenheit : ',((temp*9)/5 + 32))

def getkel(temp):
    print ('Temperature in Kelvin : ',(temp+273))

getfah(celsius)
getkel(celsius)
