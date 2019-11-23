## Exercise 61: Discount Table

prices = [4.95, 9.95, 14.95, 19.95, 24.95]
discount_amount = 60
print("Old Price | Discount | New Price")
print("--------------------------------")

for price in prices:
    new_price = round((price - (price * (discount_amount/100))), 2)
    if price < 10:
        print(f"${price}     |    {discount_amount}%    |    ${new_price}")
    else:
        print(f"${price}    |    {discount_amount}%    |    ${new_price}")
