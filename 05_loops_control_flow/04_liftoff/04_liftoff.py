def main():
    # Using a for loop
    for i in range(10, 0, -1):
        print(i, end=" ")
    print("Liftoff!")  # After the for loop finishes

    # Using a while loop
    n = 10
    while n > 0:
        print(n, end=" ")
        n -= 1
    print("Liftoff!")  # After while loop finishes

if __name__ == '__main__':
    main()
