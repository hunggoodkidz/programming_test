import random
from collections import defaultdict

def unstable_sort(flights):
    # Shuffle the list first (breaking the original order),
    # then sort by city. Because the original order was randomized,
    # flights that share the same city won't remain in their original order.
    flights = list(flights)  # copy to avoid mutating the input
    random.shuffle(flights)
    return sorted(flights, key=lambda x: x[0])

def flight_sort_demo():
    flights_by_time = [
        ("Chicago", "09:00:00"),
        ("Phoenix", "09:00:03"),
        ("Houston", "09:00:13"),
        ("Chicago", "09:00:59"),
        ("Houston", "09:01:10"),
        ("Chicago", "09:03:13"),
        ("Seattle", "09:10:11"),
        ("Seattle", "09:10:25"),
        ("Phoenix", "09:14:25"),
        ("Chicago", "09:19:32"),
        ("Chicago", "09:19:46"),
        ("Chicago", "09:21:05"),
        ("Seattle", "09:22:43"),
        ("Seattle", "09:22:54"),
        ("Chicago", "09:25:52"),
        ("Chicago", "09:35:21"),
        ("Seattle", "09:36:14"),
        ("Phoenix", "09:37:44")
    ]

    # 1. Sorted by time
    print("\nFlights (sorted by time):")
    for city, time in flights_by_time:
        print(f"  {city:10s} {time}")

    # 2. Stable sort by location
    stable_by_location = sorted(flights_by_time, key=lambda x: x[0])
    print("\nSorted by location (stable):")
    for city, time in stable_by_location:
        print(f"  {city:10s} {time}")

    # 3. Not stable sort by location
    unstable_by_location = unstable_sort(flights_by_time)
    print("\nSorted by location (not stable):")
    for city, time in unstable_by_location:
        print(f"  {city:10s} {time}")

if __name__ == "__main__":
    flight_sort_demo()
