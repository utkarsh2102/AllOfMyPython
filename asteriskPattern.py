#! /usr/bin/env python3

row = int(input("Enter the number of rows: "))
i = 1

while i <= row:
    print("*" * i)
    i += 1
    



row = int(input("Enter the number of rows: "))
i = row

while i > 0:
    print("*" * i)
    i -= 1




row = int(input("Enter the number of rows: "))
i = 1

while i <= row:
    print(" " * (row - i) + "*" * i)
    i += 1





row = int(input("Enter the number of rows: "))
i = row

while i > 0:
    print(" " * (row - i) + "*" * i)
    i -= 1
