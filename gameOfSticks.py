#! /usr/bin/env python3

from __future__ import print_function
from random import randint

"""
This is a simple stick game, where there are 21 sticks.
The one who picks up the last stick loses.
You'll be playing against the computer.
"""

STICKS = 21

print("There are 21 sticks, you make pick any number of stick(s) from 1-4.")
print("The one who picks the last stick loses.")

while True:
    print(f"{STICKS} stick(s) are left.")
    STICKS_CHOSEN = int(input("Enter the number of stick(s) you want to pick: "))
    if STICKS <= 1:
        print("Aw, you lose :/")
        break
    if STICKS_CHOSEN > 4 or STICKS_CHOSEN < 1:
        print("Duh, wrong choice!")
        continue
    STICKS -= STICKS_CHOSEN
    CHOICE = randint(1,4)
    print(f"Computer chose {CHOICE} stick(s).")
    STICKS -= CHOICE
    if STICKS <= 1:
        print("Yay, you won! :D")
        break
