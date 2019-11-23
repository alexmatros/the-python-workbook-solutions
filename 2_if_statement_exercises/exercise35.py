## Exercise 35: Dog Years

humanYears = int(input("Enter the number of human years: "))

if humanYears <= 2 and humanYears > 0:
    dogYears = humanYears * 10.5
    print(f"{humanYears} human years are equivalent to {dogYears} dog years old.")
elif humanYears > 2:
    dogYears = (humanYears - 2) * 4 + 21
    print(f"{humanYears} human years are equivalent to {dogYears} dog years old.")
else:
    print("Error. Please enter a natural number.")
