## Exercise 6: Tax and Tip

tax = 0.13
tip = 0.18

costOfMeal = float(input("Enter the cost of the meal: $"))

taxAmount = round((costOfMeal * tax), 2)
tipAmount = round((costOfMeal * tip), 2)

grandTotal = round((costOfMeal + taxAmount + tipAmount), 2)

print(f"For a meal that costs ${costOfMeal}, the tax is ${taxAmount}"
      f" and the tip will be ${tipAmount}. The grand total for the meal comes to ${grandTotal}.")
