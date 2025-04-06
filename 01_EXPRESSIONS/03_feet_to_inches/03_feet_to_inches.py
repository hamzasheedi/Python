# Conversion constant
FOOT_TO_INCH = 12

def main():
    print("=== Feet to Inches Converter ===")

    # Ask user for the length in feet
    feet = float(input("Enter the length in feet: "))

    # Convert to inches
    inches = feet * FOOT_TO_INCH

    # Display the result
    print(f"\n{feet} feet is equal to {inches} inches.")

# Entry point
if __name__ == '__main__':
    main()
