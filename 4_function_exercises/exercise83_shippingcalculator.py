def main():
    num_i = int(input("Enter the number of items: "))
    print(f"The shipping charge for {num_i} items is ${shipping_calculator(num_i)}.")


def shipping_calculator(items: int) -> float:
    """Computes the cost to ship x amount of items.
    
    Args:
        items: The number of items.
    Returns:
        The cost to ship the items.
    """
    flat_rate = 10.95
    extra_rate = 2.95
    if items > 0:
        return round((flat_rate + (extra_rate * (items - 1))), 2)
    else:
        return 0

if __name__ == "__main__":
    main()