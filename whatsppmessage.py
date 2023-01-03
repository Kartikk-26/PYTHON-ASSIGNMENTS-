import random 
import pyautogui as pg
import time
animal=('RUDRA','BODY BUILDER','BROTHER')
time.sleep(8)
for i in range(150):
    a=random.choice(animal)
    pg.write("HAPPY BIRTHDAY "+a)
    pg.press('enter')