# 📱 Phone Book Program

A simple Python console-based program to create and search contacts using a dictionary.

---

## ✅ Features

- Add contact names with phone numbers.
- Store them in a dictionary.
- Look up phone numbers by name.
- Case-insensitive "Yes/No" input handling.
- Gracefully handles missing contacts.

---

## 🚀 How It Works

1. The user is prompted to enter contact names and phone numbers.
2. Pressing Enter with no input stops the contact entry.
3. Once done, the contact list is displayed.
4. The user can then search for contact numbers by name.
5. Typing `"no"` exits the program.

---

## 💡 Example

Enter Contact Name (Press Enter to Exit): Alice

Enter Contact Number (Press Enter to Exit): 12345

Enter Contact Name (Press Enter to Exit): Bob

Enter Contact Number (Press Enter to Exit): 67890

Your Contact List: {'Alice': '12345', 'Bob': '67890'}

Do you want to search for a contact? (Yes or No): yes

Enter the contact name to look up: Alice

The number of Alice is 12345

Do you want to search for a contact? (Yes or No): no

Thanks for using the Phone Book!

## 🛠️ Concepts Used
Dictionaries for storing key-value pairs

Infinite loops with while True

Input validation

try-except removed in favor of direct dictionary checks

## 🔧 Requirements
Python 3

No external packages required
