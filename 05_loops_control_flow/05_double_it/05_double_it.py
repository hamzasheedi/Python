curr_value = int(input("Enter Your Number: "))

while True:
    curr_value *= 2
    print(f"Current Value: {curr_value}")
    if curr_value >= 100:
        print("Done! Value has reached or exceeded 100.")
        break
