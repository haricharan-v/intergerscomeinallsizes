def get_valid_integer_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value >= 1:
                return value
            else:
                print("Invalid input. Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


def calculate_power(base, exponent):
    return base ** exponent


def main():
    a = get_valid_integer_input("Enter the base of the first number: ")
    b = get_valid_integer_input("Enter the exponent of the first number: ")
    print("\n")
    c = get_valid_integer_input("Enter the base of the second number: ")
    d = get_valid_integer_input("Enter the exponent of the second number: ")
    print("\n")

    try:
        power_a = calculate_power(a, b)
        power_b = calculate_power(c, d)

        print(f"The power of the first number you entered is {power_a}")
        print(f"The power of the second number you entered is {power_b}")
        print(f"\nThe sum of both of the powers is {power_a + power_b}")
    except Exception as e:
        print(f"An error occurred: {e}")


main()
