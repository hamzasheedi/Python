def validation(user_age):
    # Voting age thresholds
    Peturksbouipo = 16
    Stanlau = 25
    Mayengua = 48

    print(f"\n📋 Voting Age Requirements:")
    print(f"Peturksbouipo: {Peturksbouipo}")
    print(f"Stanlau: {Stanlau}")
    print(f"Mayengua: {Mayengua}")

    # Eligibility check
    if user_age >= Mayengua:
        print("\n✅ You can vote in Peturksbouipo, Stanlau, and Mayengua.")
    elif user_age >= Stanlau:
        print("\n✅ You can vote in Peturksbouipo and Stanlau.")
    elif user_age >= Peturksbouipo:
        print("\n✅ You can vote in Peturksbouipo.")
    else:
        print(f"\n❌ You're too young to vote.")
        print(f"You need to be at least {Peturksbouipo} to vote in Peturksbouipo,")
        print(f"{Stanlau} for Stanlau, and {Mayengua} for Mayengua.")

def main():
    try:
        user_age = int(input("\n🔢 Enter Your Age: "))
        validation(user_age)
    except ValueError:
        print("⚠️ Please enter a valid number.")

if __name__ == '__main__':
    main()
