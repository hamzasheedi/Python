# Fruit Shop Program

fruits = {
    'Apple': 1.5,
    'Durian': 50,
    'Jackfruit': 80,
    'Kiwi': 1,
    'Rambutan': 1.5,
    'Mango': 5
}

stocks = {
    'Apple': 100,
    'Durian': 10,
    'Jackfruit': 30,
    'Kiwi': 20,
    'Rambutan': 9,
    'Mango': 4
}

def ask_user():
    print("🛒 Welcome to the Fruit Shop!")
    print("\n📦 List of Available Fruits:\n")
    
    for fruit in fruits:
        print(f"- {fruit}: ${fruits[fruit]} each | Stock: {stocks[fruit]} available")

    total = 0

    for fruit in fruits:
        try:
            quantity = int(input(f"\nHow many {fruit}s would you like? "))
        except ValueError:
            print("❌ Invalid input! Please enter a number.")
            continue

        if quantity < 0:
            print("❌ Please enter a positive number.")
            continue

        if quantity > stocks[fruit]:
            print(f"❌ Sorry! Only {stocks[fruit]} {fruit}(s) in stock.")
            continue

        total += fruits[fruit] * quantity

    print(f"\n💰 Your total bill is: ${total:.2f}")

def main():
    ask_user()

if __name__ == '__main__':
    main()
