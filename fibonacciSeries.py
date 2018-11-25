#! /usr/bin/env python3

a, b = 0, 1
count=0
number = int(input("Enter a number till where you want the series: "))

while number > b:
    print(f"{b}", end = "\t")
    a, b = b, a + b
    count+=1

print(f"\nNumber of elements are {count}")
