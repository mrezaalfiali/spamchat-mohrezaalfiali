import pyautogui as auto
import time

pesan = "all in 03 "
a = 100
time.sleep(3)

for i in range(a):
    auto.typewrite(pesan + '\n')