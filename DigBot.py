from time import sleep
from pydirectinput import press, keyDown, keyUp
from random import choice
import cv2 as cv
import numpy as np


def DigBot():

    print("Starting DigBot...")
    for i in range(1, 6)[::-1]:
        print(f"{i}")
        sleep(1)
    direction = ['up', 'left', 'down', 'right']
    print("DigBot started")

    def attack():
        for i in range(5):
            for direct1 in direction:
                press(direct1)
                for j in range(2):
                    press('s')


    def collect():
        pass

    press('down')

    counter = 0
    while True:
        for i in range(5):
            press('d')
            for j in range(2):
                press('down')

        for i in range(6):
            keyDown('up')
        keyUp('up')
        counter += 1
        print(f"Round: {counter}")

        if counter % 2 == 0:
            press('left')
        else:
            press('right')

        press('down')

        if counter % 5 == 0:
            attack()


DigBot()

