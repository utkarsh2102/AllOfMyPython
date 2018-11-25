#! /usr/bin/env python3

print("Let's calculate the largest number! :D")
a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))
c = int(input("Enter 3rd number: "))

if a > b:
    if a > c:
        print(f"Largest: {a}")
    else:
        print(f"Largest: {c}")

else:
    if b > c:
        print(f"Largest: {b}")
    else:
        print(f"Latgest: {c}")
        
