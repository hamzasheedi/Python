import hashlib

# Dictionary to store some pre-hashed passwords with their website names
passwords = {
    "16ec242fd55998a22dfac771e4424a8e10a771b20e3c0ae55f9b4c2188abfd88": "www.youtube.com",
    "f2c538e8b43927d2d71d5093261b371647d7a139709873545b763acdb118d1a8": "www.x.com"
}

def generate_password():
    while True:
        text = input("\n🔐 Enter Full Link Of Website (or press Enter to exit): ")
        if text == "":
            return
        secret = text + " hamza"  # Secret salt for extra security
        hash_object = hashlib.sha256(secret.encode())
        hash_hex = hash_object.hexdigest()
        print("✅ Generated Password Hash:", hash_hex, "\n")

def match_password():
    while True:
        text = input("\n🔍 Enter Password Hash To Match (or press Enter to exit): ")
        if text == "":
            return
        if text in passwords:
            print("\n🔗 This Password Belongs To:", passwords[text])
        else:
            print("❌ Sorry! Password not found in the records.")

def main():
    user_input = input("\nDo you want to Generate or Match your password? (Use 'Generate' or 'Match'): ").lower()

    if user_input == "generate":
        generate_password()
    elif user_input == "match":
        match_password()
    else:
        print("⚠️ Please choose 'Generate' or 'Match'.")

if __name__ == '__main__':
    main()
