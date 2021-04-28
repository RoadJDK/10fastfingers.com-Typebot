import numpy as nm
import pyautogui
import pytesseract
import time
import cv2

from pynput.keyboard import Key, Controller
from PIL import ImageGrab


keyboard = Controller()

time_running = 60
wpm = 40
accuracy = 100

def imgToString(bbox):
  
    pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
    
    cap = ImageGrab.grab(bbox)
  
    tesstr = pytesseract.image_to_string(
            cv2.cvtColor(nm.array(cap), cv2.COLOR_BGR2GRAY), 
            lang ='eng')
    return tesstr

def getArea():
    print("Press enter to get pos1 (left)")
    input()
    x1 = pyautogui.position()
    print("Press enter to get pos1 (top)")
    input()
    y1 = pyautogui.position()
    print("Press enter to get pos1 (right)")
    input()
    x2 = pyautogui.position()
    print("Press enter to get pos1 (bottom)")
    input()
    y2 = pyautogui.position()
    return (x1.x,y1.y,x2.x,y2.y)

def hasTextChanged(text,area):
    checkText = imgToString(area)
    if (text == checkText):
        return False
    else:
        return True

print('\n'*50)
print("Hello there! You wanna use this Typewriter? Perfect! Answer those questions for me please:")
print("")
print("How long does the test run?")
while(True):
    try:
        time_running = int(input())
        break
    except ValueError:
        print("That's not a real number!")
print("")
print("How many WPS you wanna achieve?")
while(True):
    try:
        wpm = int(input())
        break
    except ValueError:
        print("That's not a real number!")

area = getArea()

print("start in 5")
time.sleep(1)
print("start in 4")
time.sleep(1)
print("start in 3")
time.sleep(1)
print("start in 2")
time.sleep(1)
print("start in 1")
time.sleep(1)

text = imgToString(area)

t_end = time.time() + 60 * 60
delay = time_running / wpm

while time.time() < t_end:
    if (hasTextChanged(text,area) == True):
        text = imgToString(area)
    else:
        for c in text:
            if (c == " "):
                pyautogui.hotkey('space')
                time.sleep(delay)
            else:
                keyboard.press(c)
                time.sleep(0.00005)
        pyautogui.hotkey('space')

'''
# TODO anticheat
words = 0

if (hasTextChanged(text,area) == True):
        text = imgToString(area)
else:
    for c in text:
        newline = False
        if (words % 11 == 0 and words != 0):
            pyautogui.hotkey('enter')
            newline = True
            words = 0
        if (c == " "):
            if (newline == False):
                words += 1
            pyautogui.hotkey('space')
        else:
            keyboard.press(c)
    pyautogui.hotkey('space')
'''