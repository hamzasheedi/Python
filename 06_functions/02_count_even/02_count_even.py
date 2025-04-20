def check_even(numbers):
    print("\nEven Numbers:")
    for num in numbers:
        if num % 2 == 0:
            print(num)

def main():
    numbers = []
    while True:
        try:
            user_input = input("Enter an integer (or press Enter to stop): ")
            if user_input == "":
                break
            number = int(user_input)
            numbers.append(number)
        except ValueError:
            print("Please enter a valid integer.")

    print("\nYour Numbers:", numbers)
    check_even(numbers)

if __name__ == '__main__':
    main()
