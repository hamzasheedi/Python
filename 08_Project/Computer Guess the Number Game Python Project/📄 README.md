# 🎯 Number Guessing Game - Python Project

A simple terminal-based number guessing game where the player tries to guess a randomly generated number.

---

## 📌 Features

- Random number generation between 1 and a user-defined upper limit.
- Gives hints if the guess is too high or too low.
- Keeps running until the user guesses correctly.
- Handles invalid (non-integer) inputs gracefully.

---

## 🧠 How It Works

1. The program generates a random number using `random.randint`.
2. The user is asked to guess the number.
3. Feedback is given after each guess:
   - Too high 📈
   - Too low 📉
4. The game ends when the user guesses the correct number.

---

## ▶️ Usage

### Run the script

```bash
python number_guessing_game.py
```

## Example Output

Guess a number between 1 and 10: 5

📉 Your guess is too low.

Guess a number between 1 and 10: 8

📈 Your guess is too high.

Guess a number between 1 and 10: 7

🎉 Congrats! You guessed the number: 7


## 📦 Requirements
Python 3.x

No additional libraries required

## 📌 Tip

You can change the difficulty by modifying the upper limit passed to guess(). For example:

```
guess(100)  # Makes it more challenging!
```

## 🔒 License
Free to use for personal and educational purposes.
