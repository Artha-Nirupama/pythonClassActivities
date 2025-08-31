import time
import sys

sys.stdout.reconfigure(encoding='utf-8')

print("****⏳The count Down Timer⏳****")

userInput =int(input("Enter your time in seconds: "))
   
while userInput>0:
    secs = int(userInput%60)
    minites = int(userInput/60%60)
    hours = int(userInput/3600)
    print(f"{hours:02} : {minites:02} : {secs:02}")
    userInput-=1
    time.sleep(1)
print("Time Out!⌛")