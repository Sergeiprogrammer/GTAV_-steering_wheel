import os
import time

try:
    print("installing need time")
    os.system("pip install pygame keyboard vgamepad")
    time.sleep(2)
    print("all good")
except:
    print(Exception)