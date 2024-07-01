from main import calculate_average


if __name__ == "__main__":
    try:
        numbers = [10, 20, 30, 40, 50]
        average = calculate_average(numbers)
        print(f"The average is {average}")
    except (ValueError, TypeError) as e:
        print(f"Error: {e}")
