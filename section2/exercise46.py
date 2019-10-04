## Exercise 46: Season from Month and Day

month = input('Enter a month: ')
day = int(input('Enter a day of the month: '))
season = None

if month == 'April' or month == 'May':
    season = 'Spring'
elif month == 'June':
    if day < 21:
        season = 'Spring'
    else:
        season = 'Summer'
elif month == 'July' or month == 'August':
    season = 'Summer'
elif month == 'September':
    if day < 22:
        season = 'Summer'
    else:
        season = 'Fall'
elif month == 'October' or month == 'November':
    season = 'Fall'
elif month == 'December':
    if day < 21:
        season = 'Fall'
    else:
        season = 'Winter'
elif month == 'January' or month == 'February':
    season = 'Winter'
elif month == 'March':
    if day < 20:
        season = 'Winter'
    else:
        season = 'Spring'
else:
    print('Error. Please check your spelling for the name of the month. Ex. March.')

if season != None:
    print(f'{month} {day} is in {season}.')