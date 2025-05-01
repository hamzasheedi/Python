def get_user_data():
    """Prompts the user for personal information and returns it as a tuple."""
    first_name = input("What is your first name? ").strip()
    last_name = input("What is your last name? ").strip()
    email = input("What is your email? ").strip()
    return first_name, last_name, email

def main():
    user_data = get_user_data()
    print("\n📋 Collected User Information:")
    print(f"First Name: {user_data[0]}")
    print(f"Last Name: {user_data[1]}")
    print(f"Email: {user_data[2]}")

if __name__ == '__main__':
    main()

