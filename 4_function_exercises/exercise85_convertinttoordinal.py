def main():
    num = int(input('Enter a number from 1-12: '))
    print(f"The ordinal number for {num} is {int_to_ordinal(num)}.")

def int_to_ordinal(number: int) -> str:
    if number < 12:
        if number == 1:
            return 'first'
        elif number == 2:
            return 'second'
        elif number == 3:
            return 'third'
        elif number == 4:
            return 'fourth'
        elif number == 5:
            return 'fifth'
        elif number == 6:
            return 'sixth'
        elif number == 7:
            return 'seventh'
        elif number == 8:
            return 'eighth'
        elif number == 9:
            return 'ninth'
        elif number == 10:
            return 'tenth'
        elif number == 11:
            return 'eleventh'
        elif number == 12:
            return 'twelfth'
    else:
        return ''

if __name__ == "__main__":
    main()