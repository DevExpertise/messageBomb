import random
import pyautogui as pg
import time
s=input("Enter your lover's name:")
s=s.upper()
t=int(input("How much message  you to sent :"))
item=(" I LOVE YOU"," I LIKE YOU"," I WANT TO MARRY YOU"," YOU  LOKING BEAUTIFUL")
for i in range(t):
    a=random.choice(item)
    pg.write(s +a)
    pg.press('enter')
    