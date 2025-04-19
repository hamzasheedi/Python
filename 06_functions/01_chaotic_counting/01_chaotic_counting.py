import random

def chaotic_counting():
    for i in range(1, 11):
        print(f"\nCounting: {i}")
        if done():
            print("😅 Suddenly felt like stopping...")
            return

def done():
    DONE_LIKELIHOOD = 0.3  # 30% chance to randomly stop
    return random.random() < DONE_LIKELIHOOD

def main():
    print("🤖 I'm going to count up to 10 — unless I randomly decide to stop early!")
    chaotic_counting()
    print("✅ I'm done!")

if __name__ == "__main__":
    main()
