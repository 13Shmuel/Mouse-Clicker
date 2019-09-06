import keyboard
import mouse
import time

Config = open("Config.txt","r")
num = float(Config.read())
##start = Config.readline(3)
##end = Config.readline(5)

while True:
    if keyboard.is_pressed('q'):
        while True:
            mouse.click(button='left')
            time.sleep(num)

            if keyboard.is_pressed('w'):
                break
