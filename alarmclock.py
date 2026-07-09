import winsound
from datetime import datetime
import time
a_t="07:10:00 AM"
while True:
    c_t=datetime.now().strftime("%I:%M:%S %p")
    if c_t==a_t:
        print("Beep!!!")
        winsound.Beep(1000,3000)
        break
    time.sleep(1)
