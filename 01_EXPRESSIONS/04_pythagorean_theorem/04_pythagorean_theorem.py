import math

def main():
    print("\n=== Find the Hypotenuse Using Pythagorean Theorem ===")

    # Get input for the two perpendicular sides
    ab = float(input("Enter the length of side AB: "))
    ac = float(input("Enter the length of side AC: "))

    # Calculate the hypotenuse BC
    bc = math.sqrt(ab ** 2 + ac ** 2)

    # Display the result
    print(f"\nThe hypotenuse (BC) of the triangle is: {bc}")

# Entry point
if __name__ == '__main__':
    main()
