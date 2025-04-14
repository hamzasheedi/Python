numbers = []
unique_numbers = []
frequency = {}

def make_list():
    while True:
        element = input("\nEnter a number (or press Enter to finish): ")
        if element == "":
            break
        numbers.append(element)

def count_duplicates():
    for item in numbers:
        if item not in unique_numbers:
            unique_numbers.append(item)
            frequency[item] = 1
        else:
            frequency[item] += 1
            print(f"{item} appears {frequency[item]} times")

def main():
    make_list()
    count_duplicates()

if __name__ == '__main__':
    main()
