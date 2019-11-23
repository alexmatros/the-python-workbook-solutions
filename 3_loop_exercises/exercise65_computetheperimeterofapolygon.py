## Exercise 65: Compute the Perimeter of a Polygon

perimeter = 0

initial_x = float(input("Enter the x part of the coordinate: "))
initial_y = float(input("Enter the y part of the coordinate: "))

prev_x =  initial_x
prev_y = initial_y

x_val = input("Enter the x part of the coordinate (blank to quit): ")
while x_val != '':
	x = float(x_val)
	y = float(input("Enter the y part of the coordinate: "))
	
	distance = ((x - prev_x)**2 + (y - prev_y)**2) ** 0.5 
	perimeter += distance 
	
	prev_x = x 
	prev_y = y 

	x_val = input("Enter the x part of the coordinate (blank to quit): ")

distance = ((initial_x - x)**2 + (initial_y - y)**2) ** 0.5
perimeter += distance

print()
print(f"The perimeter of this polygon is {perimeter}.")