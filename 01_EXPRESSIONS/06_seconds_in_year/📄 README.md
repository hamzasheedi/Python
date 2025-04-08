# Years to Seconds Converter ⏳

This Python program converts a given number of **years** into **seconds**, assuming:

- 1 year = 365 days (non-leap year)
- 1 day = 24 hours
- 1 hour = 60 minutes
- 1 minute = 60 seconds

### 📐 Formula Used

1 year = 365 × 24 × 60 × 60 = 31,536,000 seconds

---
## 🧠 What It Does

1. Prompts the user to enter a number of years.
2. Multiplies that number by `31,536,000` to get the total seconds.
3. Displays the result, nicely formatted.

## 🧪 Example Output

=== Convert Years to Seconds ===

Enter the number of years to convert: 2

There are 63,072,000 seconds in 2 year(s).

---

## 🛠 Requirements

- Python 3.x

## ▶️ How to Run

1. Save the code in a file, e.g., `years_to_seconds.py`
2. Open terminal or command prompt
3. Run the file using:

python years_to_seconds.py

---

## 📚 Topics Covered

- Constants
- Floating Point Input
- Multiplication
- Formatted Output
- Program Structure

---

💡 *Want to improve it?*
You could add:
- Leap year support (`365.25` days per year)
- Convert **months** or **days** too
- Show breakdown (e.g., "X days, Y hours")
