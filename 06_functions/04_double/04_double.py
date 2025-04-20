def double(num):
    doubled = num * 2
    print(f"Double that is {doubled}")

def main():
    try:
        num = int(input("Enter Your Number To Double: "))
    except:
        print("Invalid input. Please enter a number.")
        return
    double(num)

if __name__ == '__main__':
    main()
