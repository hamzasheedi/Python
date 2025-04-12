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
        print("\n✅ You can
