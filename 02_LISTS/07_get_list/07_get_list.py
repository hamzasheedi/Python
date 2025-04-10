my_list: list[str] = []

def make_list():
    print("📥 Let's build a list! Press Enter without typing anything to finish.\n")

    while True:
        element = input("➕ Enter an element (or press Enter to finish): ")
        if element == "":
            print(f"\n✅ Final List: {my_list}")
            return
        my_list.append(element)

def main():
    make_list()

if __name__ == '__main__':
    main()
