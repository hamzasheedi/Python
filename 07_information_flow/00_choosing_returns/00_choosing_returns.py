ADULT_AGE = 18

def check_adult(age):
    return age >= ADULT_AGE  # Returns True if age is 18 or above, else False

def main():
    print("(Check if the entered age is considered adult)")
    try:
        age = int(input("How old is this person?: "))
        is_adult = check_adult(age)
        print("Is adult?", is_adult)
    except ValueError:
        print("Please enter a valid number.")

if __name__ == '__main__':
    main()
