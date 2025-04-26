def is_odd(value):
    odd = value % 2
    if odd != 0:
        print(f"{value} is Odd!")

def is_even(value):
    even = value % 2
    if even == 0:
        print(f"{value} is Even!")

def main():
    for i in range(11):
        is_even(i)
        is_odd(i)

if __name__ == '__main__':
    main()

