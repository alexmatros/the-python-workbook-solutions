from exercise85_convertinttoordinal import int_to_ordinal

def main():
    for verse in range(1, 13):
        display_verse(verse)

def display_verse(day: int) -> str:
    '''Returns the verses of the Christmas song "The Twelve Days of Christmas" based on the day of Christmas

    Args:
        day: The day of Christmas.
    Returns:
        The verse for the particular day of Christmas.
    '''
    print(f"On the {int_to_ordinal(day)} day of Christmas")
    print("My true love gave to me:")

    if day >= 12:
        print("Twelve drummers drumming")
    if day >= 11:
        print("Eleven pipers piping")
    if day >= 10:
        print("Ten lords a leaping")
    if day >= 9:
        print("Nine ladies dancing")
    if day >= 8:
        print("Eight maids a milking")
    if day >= 7:
        print("Seven swans a swimming")
    if day >= 6:
        print("Six geese a laying")
    if day >= 5:
        print("Five gold rings, badam-pam-pam")
    if day >= 4:
        print("Four calling birds")
    if day >= 3:
        print("Three French hens")
    if day >= 2:
        print("Two turtle doves")
    if day == 1:
        print("A", end=" ")
    else:
        print("And a", end=" ")
    print("partridge in a pear tree.")
    print()


if __name__ == "__main__":
    main()