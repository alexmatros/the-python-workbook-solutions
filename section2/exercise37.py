## Exercise 37: Name that Shape

numberOfSides = int(input("Enter the number of sides of a shape: "))
shape = None

if numberOfSides == 3:
    shape = "triangle"
elif numberOfSides == 4:
    shape = "quadrilateral"
elif numberOfSides == 5:
    shape = "pentagon"
elif numberOfSides == 6:
    shape = "hexagon"
elif numberOfSides == 7:
    shape = "heptagon"
elif numberOfSides == 8:
    shape = "octagon"
elif numberOfSides == 9:
    shape = "nonagon"
elif numberOfSides == 10:
    shape = "decagon"
else:
    print("Error. Please enter a number from 3 to 10.")
    
if shape != None:
    print(f"A shape with {numberOfSides} sides is a {shape}.")