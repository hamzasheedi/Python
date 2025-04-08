# Number of seconds in one year (365 days)
SECONDS_IN_YEAR = 31_536_000

def main():
    print("\n=== Convert Years to Seconds ===")

    # Get user input
    years = float(input("Enter the number of years to convert: "))

    # Convert to seconds
    seconds = years * SECONDS_IN_YEAR

    # Display result
    print(f"\nThere are {seconds:,.0f} seconds in {years} year(s).")

# Entry point
if __name__ == '__main__':
    main()
