# Write a program that generates a random number between 1 and 10 and prints your name
# that many times.

from random import randint

num1 = randint(1,10)

name1 = input("Please enter your name: ")
print("A random number between 1 and 10 is: ",num1)
print(f"Your name is printed {num1} times as follows: ")
print((name1+" ")*num1)