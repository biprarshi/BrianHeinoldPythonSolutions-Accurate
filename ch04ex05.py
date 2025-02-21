# Generate a random number between 1 and 10. Ask the user to guess the number and print a
# message based on whether they get it right or not.


from random import randint

rand_num1 = randint(1,10)
num1 = eval(input("Please enter a number between 1 and 10: "))
if rand_num1 == num1:
    print(f"Random number = {rand_num1}, number entered = {num1}. It's a match.")
else:
    print(f"Random number = {rand_num1}, number entered = {num1}. Not a match.")