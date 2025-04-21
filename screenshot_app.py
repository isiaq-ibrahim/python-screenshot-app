import time
import pyautogui

def screenshot():
    #added to generate a random int number for the image
    name = int(round(time.time() * 1000))
    # this will save the screenshots in the folder screensnaps and in .png format
    name = 'C:/Users/ibrah/Documents/LearnPythonProjects/screensnaps/{}.png'.format(name)
    time.sleep(5)
    #removed 'test.png' and replaced with name
    img = pyautogui.screenshot(name)
    img.show()

screenshot()