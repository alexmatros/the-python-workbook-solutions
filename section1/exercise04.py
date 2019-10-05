## Exercise 4: Area of a Field

sqftPerAcre = 43560
width = float(input("Enter the width of the field in feet: "))
length = float(input("Enter the length of the field in feet: "))

acres = width * length / sqftPerAcre

print(f"The area of the field is {acres} acres.")
