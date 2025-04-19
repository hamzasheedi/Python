def main():
    print("\n🔢 FIND AVERAGE OF TWO NUMBERS")
    try:
        number1 = float(input("\nEnter Number 1: "))
        number2 = float(input("Enter Number 2: "))
        average = (number1 + number2) / 2
        print(f"\n📊 The average of {number1} and {number2} is {average}")
    except ValueError:
        print("\n❌ Please enter valid numbers!")

if __name__ == '__main__':
    main()
