import pyautogui
import random
import time


x = 1
while x <3:
    
    for x in range (1):

        pyautogui.moveTo(485, 257, 2, pyautogui.easeInOutQuad) 
        
        pyautogui.click(x=485, y=257)
        time.sleep(random.randint(4, 8))

        pyautogui.moveTo(450, 439, 3, pyautogui.easeInElastic) 

        pyautogui.click(x=450, y=439)
        time.sleep(random.randint(4, 8))

        pyautogui.moveTo(442, 620, 2, pyautogui.easeInOutQuad) 
 
        pyautogui.click(x=442, y=620)
        time.sleep(random.randint(4, 8))

        pyautogui.moveTo(982, 252, 1, pyautogui.easeInElastic) 

        pyautogui.click(x=982, y=252)
        time.sleep(random.randint(4, 8))

        pyautogui.moveTo(1033, 695, 4, pyautogui.easeInOutQuad) 

        pyautogui.click(x=1033, y=695)
        time.sleep(random.randint(4, 8))
