# The Fibonacci numbers are the sequence below, where the first two numbers are 1, and each
# number thereafter is the sum of the two preceding numbers. Write a program that asks the
# user how many Fibonacci numbers to print and then prints that many.
# 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89 . . .


f_num1 = f_num2 = 1
seq_length1 = eval(input("Please enter the no of Fibonacci numbers to print: "))

if(seq_length1<1):
    print("Invalid Input")
elif(seq_length1==1):
    print("Your Fibonacci sequence is:\n1")
else:
    print("Your Fibonacci sequence is:\n1, 1", sep="", end="")
    for i in range(seq_length1-2):
        print(", ",f_num1+f_num2, sep="", end="")
        f_num2 = f_num2 + f_num1
        f_num1 = f_num2 - f_num1
print()