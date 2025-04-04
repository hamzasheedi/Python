print("\n=== Simple Addition Program ===\n")

# Asking the user to input two numbers
first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))

# Function to add two numbers
def add_numbers(a, b):
    result = a + b
    print(f"\nThe sum of {a} and {b} is: {result}")

# Main function to run the program
def main():
    add_numbers(first_number, second_number)

# Entry point of the program
if __name__ == '__main__':
    main()
