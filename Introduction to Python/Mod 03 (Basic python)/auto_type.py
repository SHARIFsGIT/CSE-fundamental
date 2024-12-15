from mpl_toolkits.mplot3d.proj3d import world_transformation
import pyautogui
from time import sleep

sleep(5)
for i in range(0, 3):
    pyautogui.write('I am Shariful', interval = 0.25)
    pyautogui.press('enter')
