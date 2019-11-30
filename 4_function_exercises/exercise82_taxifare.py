def main():
    dist_km = float(input("Enter the distance travelled (km): "))
    print(f"The taxi fare for travelling {dist_km}km is ${taxi_fare(dist_km)}.")

def taxi_fare(km_travelled: float) -> float:
    '''Returns the taxi fare based on kilometeres travelled

    Args:
        km_travelled: The distance travelled in kilometers.
    Returns:
        The taxi fare
    '''
    m_travelled = km_travelled * 1000
    base_fare = 4
    extra_fare = 0.25
    extra_distance = 140
    times_charged_extra = m_travelled // extra_distance
    return base_fare + (times_charged_extra * extra_fare)

if __name__ == "__main__":
    main()