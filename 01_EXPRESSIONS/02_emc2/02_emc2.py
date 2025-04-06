def main():
    print("=== Einstein's Mass-Energy Equivalence ===")

    # Input mass in kilograms
    mass = float(input("\nEnter mass in kilograms (kg): "))

    # Speed of light in meters per second
    c = 299_792_458

    # Energy calculation using E = mc²
    energy = mass * c**2

    # Displaying the result
    print(f"\nE = {energy} joules of energy!")

    # Formula explanation
    print("""
Formula used: E = m * c²
(E stands for energy, m for mass, and c is the speed of light in a vacuum)
""")


# Entry point of the program
if __name__ == '__main__':
    main
