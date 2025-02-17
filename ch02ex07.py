# Write a program that uses exactly four for loops to print the sequence of letters below.
# AAAAAAAAAABBBBBBBCDCDCDCDEFFFFFFG


for i in range(10):
    print("A",sep="",end="")
for i in range(7):
    print("B",sep="",end="")
for i in range(4):
    print("CD",sep="",end="")
print("E",sep="",end="")
for i in range(6):
    print("F",sep="",end="")
print("G")