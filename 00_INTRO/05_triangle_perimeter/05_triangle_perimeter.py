def main():
    print("\n=== Triangle Perimeter Calculator ===")

    # Taking user input for all three sides
    side_one = float(input("\nEnter the length of side 1: "))
    side_two = float(input("Enter the length of side 2: "))
    side_three = float(input("Enter the length of side 3: "))

    # Calculating the perimeter
    perimeter = side_one + side_two + side_three

    # Displaying the result
    print(f"\nThe perimeter of the triangle is: {perimeter}")


# Entry point of the program
if __name__ == '__main__':
    main()
