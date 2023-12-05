import unittest
from main import calculate_average


def calculate_average(sequence):
    if not sequence:
        raise ValueError("The sequence cannot be empty")

    try:
        total = sum(sequence)
        average = total / len(sequence)
        return average
    except TypeError as e:
        raise TypeError("The sequence must contain only numbers") from and

if __name__ == "__main__":
    try:
        numbers = [10, 20, 30, 40, 50]
        average = calculate_average(numbers)
        print(f"The average is {average}")
    except (ValueError, TypeError) as e:
        print(f"Error: {e}")
