actual_sum = 0
rounded_sum = 0

interrupted = False 
while not interrupted:
	price = input("Enter a price: ")
	
	if price != "":
		price = float(price)
	else:
		break
		
	actual_sum += price 
	
	price_in_pennies = price * 100
	remainder = price_in_pennies % 5
	
	if remainder > 2.5:
		price_in_pennies += 5 - remainder 
	else:
		price_in_pennies -= remainder 
	
	rounded_price = price_in_pennies * 0.01
	rounded_sum += rounded_price

print(f"The actual sum is {round(actual_sum, 2)}.")
print(f"The rounded sum paid with cash is {round(rounded_sum, 2)}.")