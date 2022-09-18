from pyautogui import press, hotkey, typewrite
from time import sleep

sleep(2)

# 提前需加入剪贴板
LOOP = 20 # 次数

for i in range(LOOP):
    hotkey("ctrl", "v")
    press("enter")
    typewrite(str(i+1))
    press("enter")
    sleep(0.1)
