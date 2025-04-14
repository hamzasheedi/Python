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

def check_range(number):
    if 1 <= number <= 10:
        print("🎯 The number is between 1 and 10.")
    elif 11 <= number <= 20:
        print("📏 The number is between 11 and 20.")
    else:
        print("📉 The number is outside the 1–20 range.")

def nested_check(number):
    if number > 0:
        print("🔍 Checking further because number is positive...")
        if number % 5 == 0:
            print("✅ It's also divisible by 5.")
        else:
            print("❌ Not divisible by 5.")
    else:
        print("⛔ Skipped deeper check because number is not positive.")

def truthy_falsy_demo():
    print("\n🔎 Testing truthy and falsy values:")
    if []:
        print("✅ Empty list is truthy.")
    else:
        print("❌ Empty list is falsy.")

    if "text":
        print("✅ Non-empty string is truthy.")

    if 0:
        print("✅ Zero is truthy.")
    else:
        print("❌ Zero is falsy.")

    if None:
        print("✅ None is truthy.")
    else:
        print("❌ None is falsy.")

def main():
    try:
        number = int(input("🔢 Enter a number: "))

        print("\n--- BASIC CHECKS ---")
        check_number_type(number)
        check_even_or_odd(number)

        print("\n--- RANGE CHECK ---")
        check_range(number)

        print("\n--- NESTED IF ---")
        nested_check(number)

        print("\n--- TRUTHY/FALSY CHECK ---")
        truthy_falsy_demo()

    except ValueError:
        print("🚫 Please enter a valid integer.")

if __name__ == '__main__':
    main()
