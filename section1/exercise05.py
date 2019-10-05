## Exercise 5: Bottle Deposits

depositOneLitre = 0.10
depositPlusOneLitre = 0.25

oneLitreBottles = int(input("Enter the number of drink containers holding one litre or less: "))
plusLitreBottles = int(input("Enter the number of drink containers holding more than one litre: "))

refund = round((oneLitreBottles * depositOneLitre) + (plusLitreBottles * depositPlusOneLitre), 2)

print(f"If you return {oneLitreBottles} drink containers holding one litre or less and {plusLitreBottles}"
       f" drink containers holding more than one litre, you will get a ${refund} refund.")
