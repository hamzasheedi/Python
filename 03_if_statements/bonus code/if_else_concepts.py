def check_number_type(number):
    if number > 0:
        print("✅ It's a positive number.")
    elif number < 0:
        print("🔻 It's a negative number.")
    else:
        print("⚪ It's zero.")

def check_even_or_odd(number):
    if number % 2 == 0:
        print("🟦 It's an even number.")
    else:
        print("🟥 It's an odd number.")


if __name__ == '__main__':
    main()
