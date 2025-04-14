import random

# Constants
NUM_COUNT: int = 10
MIN_VALUE: int = 1
MAX_VALUE: int = 100

def main():
    print(f"🎲 Generating {NUM_COUNT} random numbers between {MIN_VALUE} and {MAX_VALUE}...\n")
    for _ in range(NUM_COUNT):
        number = random.randint(MIN_VALUE, MAX_VALUE)
        print(number)

if __name__ == '__main__':
    main()
