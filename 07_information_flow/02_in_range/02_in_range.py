def in_range(n, low, high):
    if n > low and n < high:
        return True
    return False

def main():
    is_in_range = in_range(10, 1, 100)
    print(is_in_range)

if __name__ == '__main__':
    main()
