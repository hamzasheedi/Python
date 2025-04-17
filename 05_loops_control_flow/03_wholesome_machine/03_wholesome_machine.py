affirmation = "I am capable of doing anything I put my mind to."

def main():
    print("\n✨ Daily Affirmation ✨")
    print(affirmation)
    
    while True:
        user_input = input("\nType the affirmation exactly as shown above: ")
        if user_input == affirmation:
            print("✅ That's right! :)")
            return
        else:
            print("❌ That was not the correct affirmation. Please try again!")

if __name__ == '__main__':
    main()
