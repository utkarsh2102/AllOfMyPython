#! /usr/bin/env python3

sum = 0
count = 0
totalNumber = int(input("How many numbers are you considering? "))

while count < totalNumber:
    newNumber = float(input("Enter new number: "))
    sum += newNumber
    count += 1

averageNumber = float(sum)/totalNumber

print("\nTotal Sum = %.2f" %(sum))
print("Average = %.2f" %(averageNumber))

