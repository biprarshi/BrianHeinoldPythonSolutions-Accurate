# Write a program that generates a random number, x , between 1 and 50, a random number y
# between 2 and 5, and computes x^y .


from random import randint

num1 = randint(1,50)
num2 = randint(2,5)
print("A random number between 1 nd 50 is: ", num1, "\nA random number between 2 nad 5 is: ", num2)
print(num1, "**", num2, "=", num1**num2)
