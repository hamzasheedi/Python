SENTENCE_START = "My school was wild! One time, I saw a"

def main():
    print("\n=== Let's Create a Funny Sentence! ===")

    # Get user inputs
    adjective = input("Please type an adjective and press enter: ")
    noun = input("Please type a noun and press enter: ")
    verb = input("Please type a verb and press enter: ")

    # Combine the sentence parts
    full_sentence = f"{SENTENCE_START} {adjective} {noun} {verb}!"
    print("\n" + full_sentence)

# Run the main function
if __name__ == '__main__':
    main()
