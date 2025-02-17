# Write a program that asks the user for their name and how many times to print it. The pro-
# gram should print out the user’s name the specified number of times.


name1 =  input("Please enter your name: ")
repeat1 = eval(input("Please neter the no of times to repeat: "))

for i in range(repeat1):
    print("Iteration",i+1,": ", name1)