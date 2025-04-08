def main():
    print("=== Double the Numbers in a List ===")

    # Take user input
    user_input = input("Enter numbers separated by commas (e.g. 1, 2, 3): ")

    # Convert input into a list of floats
    list_of_numbers = list(map(float, user_input.split(',')))

    # Double each number using a lambda
    doubled_list = list(map(lambda x: x * 2, list_of_numbers))

    # Show the original and doubled lists
    print(f"\nOriginal List: {list_of_numbers}")
    print(f"Doubled List: {doubled_list}")

# Run the function
if __name__ == '__main__':
    main()
