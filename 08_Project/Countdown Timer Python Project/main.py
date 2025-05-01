import time

def countdown(t):
    while t:
        mins, sec = divmod(t, 60)
        timer = "{:02d}:{:02d}".format(mins, sec)
        print(timer, end="\r")  # Overwrite on the same line
        time.sleep(1)
        t -= 1
    print("00:00\n⏰ Time's Up!")

if __name__ == "__main__":
    try:
        t = int(input("Enter seconds to start countdown: "))
        countdown(t)
    except ValueError:
        print("❌ Please enter a valid number!")
