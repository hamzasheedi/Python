def print_multiple(message, repeats):
    for _ in range(repeats):
        print(message)

def main():
    while True:
        try:
            message = input("Enter Your Message: (Press Enter To Exit) ")
            if message == "":
                return
            repeats = int(input("How Many Times You Want To Repeat: "))
        except:
            print("Please Try Again!!")
            continue

        print_multiple(message, repeats)

if __name__ == '__main__':
    main()
