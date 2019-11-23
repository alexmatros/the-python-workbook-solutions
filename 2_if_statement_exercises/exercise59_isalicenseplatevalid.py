## Exercise 59: Is a License Plate Valid?

plate = input('Enter a license plate: ')

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
styleOfPlate = ''

if len(plate) == 7:
    if plate[0] in letters and plate[1] in letters and plate[2] in letters and plate[3] in letters:
        if plate[4] in numbers and plate[5] in numbers and plate[6] in numbers:
            styleOfPlate = 'new'

if len(plate) == 6:
    if plate[0] in numbers and plate[1] in numbers and plate[2] in numbers:
        if plate[3] in letters and plate[4] in letters and plate[5] in letters:
            styleOfPlate = 'old'

if styleOfPlate == 'new':
    print(f'{plate} is a newer valid license plate.')
elif styleOfPlate == 'old':
    print(f'{plate} is a older valid license plate.')
else:
    print(f'{plate} is an invalid license plate.')