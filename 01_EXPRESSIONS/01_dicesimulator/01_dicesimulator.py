import random

# Function to roll two dice and print the result
def roll_dice():
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    total = die1 + die2
    print(f"\n🎲 Die 1: {die1} | 🎲 Die 2: {die2} | ➕ Total: {total}")

# Main function to roll dice 3 times
def main():
    print("=== Rolling Dice 3 Times ===")
    for i in range(3):
        roll_dice()

# Run the program
if __name__ == '__main__':
    main()
