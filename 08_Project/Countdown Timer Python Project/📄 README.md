# ⏳ Countdown Timer - Python Project

A simple terminal-based countdown timer written in Python. It allows users to enter a time in seconds and counts down to zero with a live update.

---

## 📌 Features

- Accepts input in seconds.
- Displays time in `MM:SS` format.
- Prints live countdown in the terminal.
- Shows a "Time's Up!" message when finished.

---

## 🧠 How It Works

1. The user inputs the number of seconds.
2. The program uses a loop to:
   - Format the time using `divmod`.
   - Wait 1 second using `time.sleep(1)`.
   - Update the countdown.
3. When the timer reaches 0, it displays a final message.

---

## ▶️ Usage

### Run the script

```
python countdown_timer.py
```

## Example

Enter seconds to start countdown: 10

00:10

00:09

...

00:00

⏰ Time's Up!

## 📦 Requirements

Python 3.x

No external libraries needed.

## 🔒 License

This project is open-source and free to use for learning and educational purposes.

