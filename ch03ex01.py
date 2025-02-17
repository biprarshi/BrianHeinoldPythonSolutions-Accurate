# Write a program that generates and prints 50 random integers, each between 3 and 6.


from random import randint

print("50 random numbers between 3 and 6 are: ")
for i in range(50):
    print(i+1,"\b.", randint(3,6), end="| ")