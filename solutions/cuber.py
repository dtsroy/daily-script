import time
from pyautogui import press
import random

# https://huazhechen.gitee.io/cuber/

keys = {
	"B": lambda:press("W"),
	"L'": lambda:press("E"),
	"R": lambda:press("I"),
	"B'": lambda:press("O"),
	"D": lambda:press("S"),
	"L": lambda:press("D"),
	"U'": lambda:press("F"),
	"F'": lambda:press("G"),
	"F": lambda:press("H"),
	"U": lambda:press("J"),
	"R'": lambda:press("K"),
	"D'": lambda:press("L"),
	"M": lambda:press("5"),
	"M'": lambda:press("X"),
	"L2": lambda:press("D") or press("D"),
	"R2": lambda:press("I") or press("I"),
	"F2": lambda:press("H") or press("H"),
	"U2": lambda:press("J") or press("J"),
	"B2": lambda:press("O") or press("O"),
	"D2": lambda:press("S") or press("S"),
}

def gen_random(k):
	# 获取随机的任意长度打乱步骤
	ret = ""
	for i in range(k):
		ret += random.choice(list(keys.keys())) + " "
	return ret[:-1]

def auto():
	# 自动复原
	origin = input("input>").split(" ")
	origin.reverse()
	target = [(k + "'") if len(k)==1 else k[0] if k[1]!="2" else k for k in origin]
	
	time.sleep(3)
	for key in target:
		keys[key]()

print(gen_random(30))

auto()
