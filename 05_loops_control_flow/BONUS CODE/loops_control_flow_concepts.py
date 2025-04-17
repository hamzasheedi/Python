def loop_control_demo():
    print("🔁 FOR LOOP: Loop through a list")
    fruits = ["apple", "banana", "cherry"]
    for fruit in fruits:
        print(f"Fruit: {fruit}")

    print("\n🔁 WHILE LOOP: Count till 5")
    count = 1
    while count <= 5:
        print(f"Count: {count}")
        count += 1

    print("\n🔁 BREAK STATEMENT: Stop at banana")
    for fruit in fruits:
        if fruit == "banana":
            print("Found banana, stopping...")
            break
        print(fruit)

    print("\n🔁 CONTINUE STATEMENT: Skip banana")
    for fruit in fruits:
        if fruit == "banana":
            continue
        print(fruit)

    print("\n🔁 PASS STATEMENT: Placeholder in loop")
    for fruit in fruits:
        if fruit == "banana":
            pass  # This does nothing but code won't crash
        print(fruit)

    print("\n🔁 ELSE WITH FOR LOOP: Will run only if loop ends without break")
    for fruit in fruits:
        print(fruit)
        if fruit == "kiwi":
            break
    else:
        print("Loop completed without break!")

    

def main():
    loop_control_demo()

if __name__ == "__main__":
    main()
