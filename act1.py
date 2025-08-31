import time
import sys

sys.stdout.reconfigure(encoding='utf-8')

print("****⏳The count Down Timer⏳****")

userin =int(input("Enter your time in seconds: "))
   
while userin>0:
    secs = int(userin%60)
    minutes = int(userin/60%60)
    hours = int(userin/3600)
    print(f"{hours:02} : {minutes:02} : {secs:02}")
    userin-=1
    time.sleep(1)
print("Time Out!⌛")