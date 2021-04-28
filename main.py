import numpy as nm
import pyautogui
import pytesseract
import time
import cv2

from pynput.keyboard import Key, Controller
from PIL import ImageGrab


keyboard = Controller()

def imToString(bbox):
  
    # Path of tesseract executable
    pytesseract.pytesseract.tesseract_cmd ='C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
    
    # ImageGrab-To capture the screen image in a loop. 
    # Bbox used to capture a specific area.
    cap = ImageGrab.grab(bbox)
  
    # Converted the image to monochrome for it to be easily 
    # read by the OCR and obtained the output String.
    tesstr = pytesseract.image_to_string(
            cv2.cvtColor(nm.array(cap), cv2.COLOR_BGR2GRAY), 
            lang ='deu')
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
    checkText = imToString(area)
    if (text == checkText):
        return False
    else:
        return True

print('\n'*50)
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

text = imToString(area)

while(True):
    if (hasTextChanged(text,area) == True):
        text = imToString(area)
    else:
        for c in text:
            if (c == " "):
                pyautogui.hotkey('space')
            else:
                keyboard.press(c)
                time.sleep(0.01)
        pyautogui.hotkey('space')
