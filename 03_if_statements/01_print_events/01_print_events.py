def all_loops():
    print("\n1️⃣ EVEN NUMBERS TILL 20 USING WHILE LOOP")
    while_loop = 0
    while while_loop <= 20:
        print(while_loop)
        while_loop += 2

    print("\n2️⃣ EVEN NUMBERS TILL 20 USING FOR LOOP")
    for i in range(0, 21, 2):
        print(i)

    print("\n3️⃣ EVEN NUMBERS TILL 20 USING CONDITIONAL WHILE LOOP")
    if_loop = 0
    while True:
        if if_loop > 18:
            break
        if_loop += 2
        print(if_loop)

    print("\n4️⃣ EVEN NUMBERS TILL 20 USING MULTIPLICATION (FOR LOOP)")
    for i in range(1, 11):
        print(i * 2)

def main():
    all_loops()

if __name__ == '__main__':
    main()
