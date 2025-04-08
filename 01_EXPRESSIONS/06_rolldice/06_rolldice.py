import random

def main():
    print("=== Rolling Two Dice ===")

    # Roll two dice
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    total = die1 + die2

    # Show the result
    print(f"\n🎲 Die 1: {die1}")
    print(f"🎲 Die 2: {die2}")
    print(f"➕ Total: {total}")

# Entry point
if __name__ == '__main__':
    main()
