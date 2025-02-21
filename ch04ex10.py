# Write a multiplication game program for kids. The program should give the player ten ran-
# domly generated multiplication questions to do. After each, the program should tell them
# whether they got it right or wrong and what the correct answer is.
# Question 1: 3 x 4 = 12
# Right!
# Question 2: 8 x 6 = 44
# Wrong. The answer is 48.
# ...
# ...
# Question 10: 7 x 7 = 49
# Right.

from random import randint

for i in range(10):
    num1 = randint(1,10)
    num2 = randint(1,10)
    result1 = eval(input(f'Question {i+1}: {num1} X {num2} = '))
    if result1 == num1 * num2:
        print('Right!')
    else:
        print(f'Wrong. The answer is {num1*num2}.')