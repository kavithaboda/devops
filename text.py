import random
import pyautogui as pg
import time
words = ('dumb','donkey','stupid')
time.sleep(8)
for i in range(100):
    a = random.choice(words)
    pg.write("you are a" + a)
    pg.press('enter')