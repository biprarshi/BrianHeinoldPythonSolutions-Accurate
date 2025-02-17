# Write a program that asks the user for a number and prints out the factorial of that number.

from math import factorial

num1 = eval(input("Please enter a number: "))
fact1 = factorial(num1)

# fact1 = 1
# for i in range(num1,0,-1):
#     fact1 = fact1 * i

print(f'The factorial of {num1} is: {fact1}.')