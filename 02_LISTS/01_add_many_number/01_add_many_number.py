def main():
    print("=== Sum of Numbers from a Comma-Separated List ===")

    # Get user input
    user_input = input("Enter numbers separated by commas (e.g. 1, 2, 3): ")

    # Convert the input string to a list of floats
    list_of_numbers = list(map(float, user_input.split(',')))

    # Calculate the sum
    total_sum = sum(list_of_numbers)

    # Display the result
    print(f"\nThe total sum of the numbers is: {total_sum}")

# Entry point
if __name__ == '__main__':
    main()
