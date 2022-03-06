import pyautogui #pip install PyAutoGUI
import time
a = 0
while a <= 1000:
    time.sleep(3)
    pyautogui.typewrite('hello')
    pyautogui.press('enter')
    a += 1
