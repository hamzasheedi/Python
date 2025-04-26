def get_name():
    name = input("Enter Your Name: ")
    return name

def main():
    name = get_name()
    print("Howdy", name, "! 🤠")

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()
