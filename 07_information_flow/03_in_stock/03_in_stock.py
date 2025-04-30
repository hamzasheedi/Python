stock = {"apple": 3, "mango": 4, "pineapple": 5}

def num_in_stock(fruit_name):
    if fruit_name in stock:
        inventory = stock[fruit_name]
        print(f"\nThere are {inventory} {fruit_name}(s) in stock.")
        return inventory
    return None

def main():
    print("🔍 Fruit Inventory Checker")
    while True:   
        fruit_name = input("\nEnter fruit name (or press Enter to exit): ").strip().lower()
        if fruit_name == "":
            print("Exiting inventory check. Goodbye!")
            break
        result = num_in_stock(fruit_name)
        if result is None:
            print("❌ This fruit is not in inventory. Please check your spelling.")

if __name__ == '__main__':
    main()
