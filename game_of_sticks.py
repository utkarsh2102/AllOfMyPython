#! /usr/bin/env python3

''' This is a simple stick game, where there are 21 sticks.
    The one who picks up the last stick loses.
    You'll be playing against the computer. '''

from random import randint

STICKS = 21

print("There are 21 sticks, you make pick any number of stick(s) from 1-4."
      "The one who picks the last stick loses.")

while True:
    print("{} stick(s) are left.".format(STICKS))

    STICKS_CHOSEN = int(input("Enter the number of stick(s) you want to pick: "))
    if STICKS_CHOSEN not in range(1, 5):
        print("Duh, wrong choice!")
        continue
    STICKS -= STICKS_CHOSEN
    if STICKS < 1:
        print("Aw, you lose :/")
        break
    elif STICKS == 1:
        print("Yay, you won! :D")
        break

    CHOICE = randint(1, 4)
    print("Computer chose {} stick(s).".format(CHOICE))
    STICKS -= CHOICE
    if STICKS < 1:
        print("Yay, you won! :D")
        break
    if STICKS == 1:
        print("Aw, you lose :/")
        break
