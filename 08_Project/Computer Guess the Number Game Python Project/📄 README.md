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
