# Phone Book Program

phonebook = {}

def phone_book():
    while True:
        name = input("\nEnter Contact Name (Press Enter to Exit): ")
        if name == "":
            break
        number = input("Enter Contact Number (Press Enter to Exit): ")
        if number == "":
            break
        phonebook[name] = number

def lookup():
    while True:
        response = input("\nDo you want to search for a contact? (Yes or No): ").strip().lower()
        if response == "yes":
            name = input("Enter the contact name to look up: ")
            if name in phonebook:
                print(f"The number of {name} is {phonebook[name]}")
            else:
                print("This name is not in the phone book.")
        elif response == "no":
            print("Thanks for using the Phone Book!")
            break
        else:
            print("Please enter only 'Yes' or 'No'.")

def main():
    phone_book()
    print("\nYour Contact List:", phonebook)
    lookup()

if __name__ == '__main__':
    main()
