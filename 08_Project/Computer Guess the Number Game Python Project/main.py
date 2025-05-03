import random

def guess(x):
    number = random.randint(1, x)
    guess = 0
    while guess != number:
        try:
            guess = int(input(f"Guess a number between 1 and {x}: "))
            if guess > number:
                print("📈 Your guess is too high.")
            elif guess < number:
                print("📉 Your guess is too low.")
        except ValueError:
            print("❌ Please enter a valid number.")
    print(f"🎉 Congrats! You guessed the number: {number}")

if __name__ == "__main__":
    guess(10)
