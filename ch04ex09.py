# Write a program that asks the user to enter a number and prints out all the divisors of that
# number. [Hint: the % operator is used to tell if a number is divisible by something. See Section
# 3.2.]


from math import sqrt

num1 = eval(input("Please enter a number: "))
print(f'The divisors of {num1} are: 1',end='')
for i in range(2, num1//2+1):
    if num1%i == 0:
        print(f", {i}",end='')
print(f' and {num1}.')