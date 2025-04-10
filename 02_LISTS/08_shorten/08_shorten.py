my_list = []

def make_list():
    while True:
        element = input("\n➕ Enter an element to add to the list (press Enter to finish): ")
        if element == "":
            print(f"\n📋 Your Full List: {my_list}")
            break
        my_list.append(element)

def shorten():
    removed_items = []

    # Remove elements if list is longer than 3
    while len(my_list) > 3:
        removed_items.append(my_list.pop())

    if removed_items:
        removed_items.reverse()
        print("\n⚠️ Max List Length is 3. Removing extras...")
        print(f"🗑️ Removed Elements: {'  '.join(removed_items)}")
        print(f"📤 List of Removed Items: {removed_items}")

def main():
    make_list()
    shorten()

    if len(my_list) >= 3:
        print(f"\n✅ Final List (max 3 elements): {my_list}")
    else:
        print(f"\n✅ Final List: {my_list}")

if __name__ == '__main__':
    main()
