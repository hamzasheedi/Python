# Initialize an empty list to hold repeated values
my_list: list[str] = []

def add_three_copy(target_list: list[str], data: str) -> None:
    """
    Appends the given data to the target list three times.
    """
    for _ in range(3):
        target_list.append(data)

def main():
    message = "Hello World"
    print(f"📝 Message: {message}")
    print(f"📂 List Before: {my_list}")

    # Call the function to add three copies of the message
    add_three_copy(my_list, message)

    print(f"📂 List After: {my_list}")

if __name__ == '__main__':
    main()
