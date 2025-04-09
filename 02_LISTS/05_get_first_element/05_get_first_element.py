def get_first_element():
    my_list: list[str] = []

    try:
        n = int(input("🔢 How many elements do you want to enter? "))

        for i in range(n):
            element = input(f"Enter element {i} (or press Enter to stop): ")
            if element == "":
                break
            my_list.append(element)

        if my_list:
            print(f"✅ Your first element is: {my_list[0]}")
        else:
            print("⚠️ No elements were added to the list.")

    except ValueError:
        print("❌ Please enter a valid number.")

def main():
    get_first_element()

if __name__ == '__main__':
    main()
