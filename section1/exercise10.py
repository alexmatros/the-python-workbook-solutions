## Exercise 10: Arithmetic

import math

a = int(input("Enter the first integer: "))
b = int(input("Enter the second integer: "))

sm = a + b
difference = a - b
product = a * b
quotient = a / b
remainder = a % b
log10 = math.log10(a)
exponent = a ** b

print(f"The sum of {a} and {b} is {sm}.")
print(f"The difference of {b} taken away from {a} is {difference}.")
print(f"The product of {a} multiplied by {b} is {product}.")
print(f"The quotient of {a} divided by {b} is {quotient}.")
print(f"The remainder of {a} divided by {b} is {remainder}.")
print(f"The result of log10 {a} is {log10}.")
print(f"The result of {a} to the power of {b} is {exponent}.")