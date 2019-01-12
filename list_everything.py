#!  /usr/bin/env python3

"""This snippet uses every method present in the list.
Doing this would enhance my code rating :P"""

from __future__ import print_function

# list = [int(x) for x in input().split()]
# print(list)

# Hacking my way out :P
MY_LIST = []
X = int(input("Enter the number of elements you want to enter: "))
for i in range(X):
    VAR_1 = input("Enter the element: ")
    MY_LIST.append(VAR_1)

# Printing what you entered using loops:3
print("\nThe list you entered is:")
for i in range(X):
    print(MY_LIST[i])

# Checking if the items exist? :o
print("\nI'll do some list checking for you.")
VAR_2 = input("Enter what you want to check? ")
if VAR_2 in MY_LIST:
    print("Hell yeah! It exists!")
else:
    print("Ah, entry not found. Sad life.")

# Want to know the length of the list, eh?
print("\nWant to know the length of the list? Press Y for the same.")
VAR_3 = input()
if VAR_3 == "Y":
    print(len(MY_LIST))
else:
    pass

# Insert an element wherever you want :D
VAR_4 = int(input("\nEnter the position of element you want to enter the value at: "))
VAR_5 = input("Enter the element you want to insert: ")
MY_LIST.insert(VAR_4-1, VAR_5)
print(MY_LIST)

# Let's pop something out of the way? ;)
VAR_6 = int(input("\nEnter the position of element you want to pop it from: "))
MY_LIST.pop(VAR_6-1)
print(MY_LIST)

# Oh let's go back to the start!
print("\nShould we clear the list now? Press Y for the same.")
VAR_7 = input()
if VAR_7 == "Y":
    MY_LIST.clear()
else:
    pass
print(MY_LIST)

# Good game, well played :P
print("\nGGWP!")
