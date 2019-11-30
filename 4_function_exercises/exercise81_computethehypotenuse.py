def main():
    s1, s2 = float(input("Enter the side length of the first side: ")), float(input("Enter the side length of the second side: "))
    hypotenuse = find_hypotenuse(s1, s2)
    print(f"The side length of the hypotenuse is {hypotenuse}.")

def find_hypotenuse(side_1: float, side_2: float) -> float:
    """Computes the hypotenuse of a triangle given the other 2 sides.
    
    Args:
        side_1: The side length of the first side.
        side_2: The side length of the second side.
    Returns:
        The side length of the hypotenuse.
    """
    return ((side_1 ** 2) + (side_2 ** 2)) ** (1/2)

if __name__ == "__main__":
    main()