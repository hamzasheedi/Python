import random

def main():
    number = random.randint(0, 99)
    print("\n🎯 Guess My Number!")
    print("I am thinking of a number between 0 and 99...")

    while True:
        try:
            user_guess = int(input("\nEnter your guess: "))
        except ValueError:
            print("⚠️ Please enter a valid number!")
            continue

        if user_guess < 0 or user_guess > 99:
            print("🚫 Input must be between 0 and 99!")
            continue

        if user_guess < number:
            print("🔽 Too low! Try again.")
        elif user_guess > number:
            print("🔼 Too high! Try again.")
        else:
            print(f"✅ Congrats! You guessed it right. The number was: {number}")
            break

if __name__ == '__main__':
    main()
