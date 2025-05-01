def subtract_7(num):
    """Subtracts 7 from the given number and prints the result."""
    result = num - 7
    print(f"Result after subtracting 7: {result}")

def main():
    try:
        num = int(input("Enter your number: "))
        subtract_7(num)
    except ValueError:
        print("❌ Please enter a valid integer.")

if __name__ == '__main__':
    main()
