def print_ones_digit(numb):
    last_digit = numb % 10
    print(f"The ones digit is: {last_digit}")

def main():
    while True:
        try:
            numb = int(input("Enter Your Number (Press Enter To Exit): "))
            print_ones_digit(numb)
            break
        except:
            print("Invalid input. Please enter a valid integer.")

if __name__ == '__main__':
    main()
