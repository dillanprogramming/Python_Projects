import ctypes
import random
import time

path = "file path"
imgs = ["a.jpg","b.jpg","c.jpg"]

while True:
    ctypes.windll.user32.SystemParametersInfoW(20, 0, path+imgs[random.randint(0,2)], 0)
    time.sleep(1800)
