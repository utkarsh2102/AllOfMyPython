#! /usr/bin/env python3

i = 1
num = int(input("Enter the number you want tables for: "))
print("-" * 75)

while i <= num:
    n = 1
    while n < 11:
        print(i * n, end = "\t")
        n += 1
    print()
    i += 1
