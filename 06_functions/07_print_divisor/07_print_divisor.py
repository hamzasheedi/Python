def print_divisors(num):
    for i in range(1, num + 1):
        divisor = num % i
        if divisor == 0:
            print(i)

def main():
    while True:
        try:
            num = int(input("Enter Your Number To Print Divisors: "))
        except:
            print("Input Only Integers")
            break
        print_divisors(num)

if __name__ == '__main__':
    main()

