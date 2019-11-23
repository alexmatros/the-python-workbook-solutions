## Exercise 11: Fuel Efficiency

conversionRate = 235.215

americaFuelEfficiency = int(input("Enter the fuel efficiency of a vehicle"
                            "(MPG): "))

canadaFuelEfficiency = round((conversionRate / americaFuelEfficiency), 4)

print(f"A vehicle with {americaFuelEfficiency} MPG fuel efficiency is" 
      f" equivalent to a vehicle with {canadaFuelEfficiency} L/100km fuel"
      " efficiency.")