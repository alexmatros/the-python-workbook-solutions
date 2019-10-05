## Exercise 9: Compound Interest

compoundInterest = 1.04

amtDeposited = int(input("Enter the amount deposited in your savings account: "))

totalAfter1Year = round((amtDeposited * compoundInterest), 2)
totalAfter2Years = round((totalAfter1Year * compoundInterest), 2)
totalAfter3Years = round((totalAfter2Years * compoundInterest), 2)

print(f"You have ${amtDeposited} deposited in your savings account."
      f" After 1 year, you will have ${totalAfter1Year}."
      f" After 2 years you will have ${totalAfter2Years}."
      f" After 3 years you will have ${totalAfter3Years}.")
