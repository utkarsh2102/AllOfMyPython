#!  /usr/bin/env python3

# list = [int(x) for x in input().split()]
# print(list)

# Hacking my way out :P
myList = []
x = int(input("Enter the number of elements you want to enter: "))
for i in range(x):
    var1 = input("Enter the element: ")
    myList.append(var1)

# Printing what you entered using loops:3
print("\nThe list you entered is:")
for i in range(x):
    print(myList[i])

# Checking if the items exist? :o
print("\nI'll do some list checking for you.")
var2 = input("Enter what you want to check? ")
if var2 in myList:
    print("Hell yeah! It exists!")
else:
    print("Ah, entry not found. Sad life.")

# Want to know the length of the list, eh?
print("\nWant to know the length of the list? Press Y for the same.")
var3 = input()
if var3 == "Y":
    print(len(myList))
else:
    pass

# Insert an element wherever you want :D
var4 = int(input("\nEnter the position of element you want to enter the value at: "))
var5 = input("Enter the element you want to insert: ")
myList.insert(var4-1, var5)
print(myList)

# Let's pop something out of the way? ;)
var6 = int(input("\nEnter the position of element you want to pop it from: "))
myList.pop(var6-1)
print(myList)

# Oh let's go back to the start!
print("\nShould we clear the list now? Press Y for the same.")
var7 = input()
if var7 == "Y":
    myList.clear()
else:
    pass
print(myList)

# Good game, well played :P
print("\nGGWP!")
