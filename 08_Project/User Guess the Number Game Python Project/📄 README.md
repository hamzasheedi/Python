# 🎯 Number Guessing Game (Python)

A simple command-line number guessing game where the player has to guess the randomly chosen number.

---

## 🚀 Features

- Random number generation
- Hint messages if the guess is too high or too low
- Handles invalid input gracefully
- Loop continues until the correct guess is made

---

## 🧠 How It Works

1. A number between 1 and a given limit (default 10) is randomly chosen.
2. The user keeps guessing until they find the right number.
3. Helpful hints guide the player after each attempt.

---

## 📦 Requirements

- Python 3.x

No external libraries are required.

---

## ▶️ How to Run

1. Save the code in a file named `number_guessing_game.py`.
2. Run it using the terminal:

```bash
python number_guessing_game.py
```

## 📋 Example Output

Guess a number between 1 and 10: 5

📉 Your guess is too low.

Guess a number between 1 and 10: 9

📈 Your guess is too high.

Guess a number between 1 and 10: 7

🎉 Congrats! You guessed the number: 7


## ✍️ Customize Difficulty
You can increase the difficulty by changing the guess(10) call at the end of the script. Example:

```
guess(50)  # Number will be between 1 and 50
```

## 📜 License
This project is free to use for educational and personal purposes.


