## Exercise 61: Average

keep_looping = True
total = 0
nums = 0
while keep_looping:
    num = int(input())
    if num == 0:
        keep_looping = False
    else:
        total += num
        nums += 1

if total == 0:
    print("Error. The first number cannot be 0.")
else:
    print(f"The average of the numbers entered is {total / nums}.")