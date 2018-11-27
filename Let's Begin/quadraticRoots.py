#! /usr/bin/env python3

import math

a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))
c = int(input("Enter 3rd number: "))
d = (b * b) - 4 * (a * c)
print(f"D = {d}")

if d < 0:
    print("So you are imagining..")
else:
    root1 = (-b + math.sqrt(d)) / (2 * a)
    root2 = (-b - math.sqrt(d)) / (2 * a)
    print(f"Root 1 = {root1}")
    print(f"Root 2 = {root2}")
