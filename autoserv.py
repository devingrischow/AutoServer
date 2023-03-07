from tkinter.messagebox import NO
from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api
import win32con

time.sleep(1)
print('begin')
def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

img = pyautogui.screenshot('region_tester.png',region=(0,0,2538,972))
print('region=(50,40,2500,300)')
while True:
    if pyautogui.locateOnScreen('appacheLOCATE.png', confidence=.8) != None:
        apacheArea = pyautogui.locateOnScreen('appacheLOCATE.png', confidence=.8)
        print(apacheArea[0],apacheArea[1])
        startAreaimg = pyautogui.screenshot('IMGAREA_tester.png',region=(apacheArea[0],apacheArea[1],400,25))
        if pyautogui.locateOnScreen('StartButton.png', region=(apacheArea[0],apacheArea[1],400,25),confidence=.8) != None:
            xb,yb = pyautogui.locateOnScreen('StartButton.png',region=(apacheArea[0],apacheArea[1],400,25), grayscale = False, confidence=.7)
            click(xb,yb)
            
    else:
        print("NOT ON SCREEN")
    