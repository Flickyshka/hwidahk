from termcolor import colored, cprint
from time import sleep
import time
import progress
from progress.bar import ShadyBar
import readchar
import ctypes
ctypes.windll.kernel32.SetConsoleTitleW ("Fall Guys Hack")

print('''

█▀▀ ▄▀█ █░░ █░░ █▀▀ █░█ █▄█ █▀   █▀ █▀█ █▀▀ █▀▀ █▀▄ █░█ ▄▀█ █▀▀ █▄▀   ▄█ ░ ▄█ ▀█
█▀░ █▀█ █▄▄ █▄▄ █▄█ █▄█ ░█░ ▄█   ▄█ █▀▀ ██▄ ██▄ █▄▀ █▀█ █▀█ █▄▄ █░█   ░█ ▄ ░█ █▄''')
print(" ")
sleep(2)
print("Starting download...")
sleep(1.5)

bar = ShadyBar('Processing', max=100)
for i in range(100):
    sleep(0.05)
    bar.next()
sleep(1)
print(" Finished!")
sleep(1)
print("You can open Fall Guys")
sleep(1)
print("Press Any Key To Exit")
k = readchar.readchar()

