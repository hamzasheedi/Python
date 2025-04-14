# 🔐 Password Hash Generator & Matcher

This Python tool helps you **generate** a secure password hash for a website or **match** an existing password hash with its corresponding website name.

---

## 💡 Features

- 🧪 Uses SHA-256 hashing
- 🔑 Automatically salts input with a static string
- 📖 Can match a hash with a pre-saved dictionary of known passwords
- 🛡️ No original passwords are stored — only hashes

---

## 📦 Usage

### ✅ To Generate a Hashed Password

1. Run the script.
2. Choose **"Generate"**.
3. Enter the full website URL (e.g., `www.youtube.com`).
4. You will receive a hashed password.

### 🔍 To Match an Existing Hash

1. Run the script.
2. Choose **"Match"**.
3. Enter the full SHA-256 password hash.
4. It will tell you the website it's associated with (if it's in the saved list).

---

## 📌 Example

Do you want to Generate or Match your password? (Use 'Generate' or 'Match'): generate

🔐 Enter Full Link Of Website (or press Enter to exit): www.youtube.com

✅ Generated Password Hash: 16ec242fd55998a22dfac771e4424a8e10a771b20e3c0ae55f9b4c2188abfd88


---

## 📁 Pre-Saved Hashes

passwords = {
    "16ec242fd55998a22dfac771e4424a8e10a771b20e3c0ae55f9b4c2188abfd88": "www.youtube.com",
    "f2c538e8b43927d2d71d5093261b371647d7a139709873545b763acdb118d1a8": "www.x.com"
}

## 🧠 Concepts Covered

Dictionaries

Input validation

Hashing with hashlib

Loops and conditions

Secure password practices

## 🛠️ Requirements

Python 3.x

No external libraries needed

## 📌 Note
This is not meant for production use. It's a fun way to understand how hashing and password matching can work behind the scenes!
