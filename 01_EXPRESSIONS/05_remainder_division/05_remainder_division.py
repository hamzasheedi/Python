def main():
    print("=== Divide Two Numbers ===")

    # Take input from user
    number_first = float(input("Enter your first number: "))
    number_second = float(input("Enter your second number: "))

    # Perform division
    answer = number_first / number_second
    remainder = number_first % number_second

    # Display result
    print(f"\nQuotient: {answer:.2f}")
    print(f"Remainder: {remainder}")

# Entry point of the program
if __name__ == '__main__':
    main()
