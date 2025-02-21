# Write a program that asks the user for two numbers and prints Close if the numbers are
# within .001 of each other and Not close otherwise.

num1 = eval(input("Please enter first number: "))

num2 = eval(input("Please enter second number: "))

if round(abs(num1 - num2),8) <= 0.001:
    print("Close")
else:
    print("Not close")
