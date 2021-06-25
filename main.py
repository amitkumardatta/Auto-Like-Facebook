import time

import pyautogui
pyautogui.FAILSAFE = False
for i in range (0,100) :
    time.sleep(3)
    pyautogui.press ('j')
    time.sleep(2)
    pyautogui.press('l')
    time.sleep(2)
    pyautogui.press('tab')
    pyautogui.press('enter')


