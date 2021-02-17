import pyscreenshot
import pytesseract as tess
tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe' #you should set this to where tesseract is installed on your pc
import pyautogui
import random
import time
import keyboard
nonbreak= True 
abc = "QWERTYUIOPASDFGHJKLZXCVBNMqwertyuopasdfghjklizxcvbnm'" #characters
while 1:
    print("Press 1 when your cursor is on top left corner of the area you want to scan")
    keyboard.wait("1")
    cmx1,cmy1= pyautogui.position()
    print("Press 2 when your cursor is on top left corner of the area you want to scan")
    keyboard.wait("2")
    cmx2,cmy2= pyautogui.position()
    print("Click enter when your cursor is in the position you want for it to type, it will automatically click and start to type everything that is in the area you selected")
    keyboard.wait("enter")
    pyautogui.click() 
    print("hold q to stop")
    word = ""
    while nonbreak:
        img = pyscreenshot.grab(bbox=(cmx1,cmy1,cmx2,cmy2)) #takes screenshot of area you selected
        text = tess.image_to_string(img) #reads the screenshot
        if text == "":
            break
        for a in range(0,len(text)):
            if keyboard.is_pressed('q'):  
                print('quitting')
                nonbreak=False
                break
            
            if text[a] in abc:
                word = word + text[a]#adds the letter to word if its in the characters
            else:
                pyautogui.write(word)#writes the word 
                word = ""
                pyautogui.press('space')
    time.sleep(0.01)
