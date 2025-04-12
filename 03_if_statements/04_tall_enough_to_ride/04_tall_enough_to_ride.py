def main():
    print("🎢 Welcome to the Ride Height Checker!")

    while True:
        try:
            height_input = input("📏 Enter your height in cm (or press Enter to quit): ")

            # Exit condition
            if height_input == "":
                print("👋 Exiting the program. Have a great day!")
                break

            # Convert input to integer
            height = int(height_input)

            # Height check
            if height >= 100:
                print("✅ You're tall enough to ride!")
            else:
                print("❌ You're not tall enough to ride. Maybe next year!")

        except ValueError:
            print("⚠️ Please enter a valid number for height.")

if __name__ == '__main__':
    main()
