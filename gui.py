import pyautogui
from pyautogui import ImageNotFoundException
import time

pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True

try:
    button = pyautogui.locateOnScreen('image.png')
    center = pyautogui.center(button)
    pyautogui.click(center)
except ImageNotFoundException:
    print('Image match not found')

pyautogui.click(400, 700)
# pyautogui.typewrite("Hello World!")
pyautogui.keyDown('shift'); pyautogui.press('4'); pyautogui.keyUp('shift')

timer = 5
while timer > 0:
    print(timer)
    time.sleep(1)
    timer -= 1
distance = 200
pyautogui.click()
while distance > 0:
    pyautogui.dragRel(distance, 0, duration=0)
    distance -= 5
    pyautogui.dragRel(0, distance, duration=0)
    pyautogui.dragRel(-distance, 0, duration=0)
    distance -= 5
    pyautogui.dragRel(0, -distance, duration=0)

