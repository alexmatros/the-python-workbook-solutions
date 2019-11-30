def main():
    x = float(input("Enter the first number: "))
    y = float(input("Enter the second number: "))
    z = float(input("Enter the third number: "))
    print(f"The median of {x}, {y} and {z} using the simple method is {simple_median(x, y, z)}")
    print(f"Using the creative method, the median is {mathematical_median(x, y, z)}")


def simple_median(a: float, b: float, c: float) -> float:
    """Returns the median of three numbers using if statements.
    
    Args:
        a: The first number.
        b: The second number.
        c: The third number.
    Returns:
        The median of a, b, c.
    """
    if a > b and b > c:
        return b
    elif c > b and b > a:
        return b
    elif c > a and a > b:
        return a
    elif b > a and a > c:
        return a
    elif a > c and c > b:
        return c
    elif b > c and c > a:
        return c


def mathematical_median(a: float, b: float, c: float) -> float:
    """Computes the median of three numbers using math and the min and max functions.
    
    Args:
        a: The first number.
        b: The second number.
        c: The third number.
    Returns:
        The median of a, b, c.
    """
    total = a + b + c
    smallest, largest = min(a, b, c), max(a,b,c)
    return total - smallest - largest

if __name__ == "__main__":
    main()