## Exercise 61: Discount Table

print("Celcius | Fahrenheit")
print("--------------------")
for celcius in range(0, 100, 10):
    fahrenheit = round((celcius * (9/5)) + 32)
    if celcius < 10:
        print(f"   {celcius}    |    {fahrenheit}")
    else:
        print(f"   {celcius}   |    {fahrenheit}")