## Exercise 38: Month Name to Number of Days

month = input("Enter the name of a month: ")
monthCheck = month.lower()
monthWith31 = ['january', 'march', 'may', 'july', 'august', 'october', 'december']
monthWith30 = ['april', 'june', 'september', 'november']

if monthCheck in monthWith31:
    print(f"{month} has 31 days.")
elif monthCheck in monthWith30:
    print(f"{month} has 30 days.")
elif monthCheck == 'february':
    print(f"{month} has 28 days in a common year and 29 days in a leap year.")
else:
    print("Error. Please check your spelling.")