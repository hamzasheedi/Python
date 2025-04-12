def main():
    try:
        years_day = int(input("📅 Enter the number of days in the year to check: "))

        if years_day == 366:
            print("✅ That's a leap year!")
        elif years_day == 365:
            print("❌ That's not a leap year.")
        else:
            print("⚠️ Invalid input. A year usually has either 365 or 366 days.")
    except ValueError:
        print("⚠️ Please enter a valid number.")

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()
