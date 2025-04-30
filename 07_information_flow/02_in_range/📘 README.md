# 🔎 In-Range Checker

A simple Python program to check if a number falls **strictly between** two bounds.

## ✅ Example

```
in_range(10, 1, 100)
# Output: True
```
The function returns True if n > low and n < high, otherwise False.

## 🧠 Key Concepts
Conditional Logic: Uses basic comparison operators (>, <)

Functions: Encapsulates logic inside reusable in_range() function

Boolean Return: Function returns a True or False value

## ▶️ How to Run
Save the script as in_range_checker.py and run it in a terminal:
python in_range_checker.py

## 📌 Notes
The check is strictly between, so the boundaries are not included.

If you want to include the bounds (e.g. low ≤ n ≤ high), change the condition to:

if low <= n <= high:
