import time
import sys
sys.stdout.reconfigure(encoding='utf-8')

print("****⏳ The Count Down Timer ⏳****")

try:
    userInput = int(input("Enter your time in seconds: "))
    if userInput <= 0:
        print("Please enter a positive number!")
    else:
        while userInput > 0:
            secs = userInput % 60
            minutes = (userInput // 60) % 60
            hours = userInput // 3600

            # overwrite same line
            sys.stdout.write(f"\r{hours:02}:{minutes:02}:{secs:02}")
            sys.stdout.flush()

            time.sleep(1)
            userInput -= 1

        print("\nTime Out!⌛")
except ValueError:
    print("Invalid input! Please enter a number.")
