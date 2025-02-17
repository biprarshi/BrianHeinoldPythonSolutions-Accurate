# Write a program that asks the user for a number of seconds and prints out how many minutes
# and seconds that is. For instance, 200 seconds is 3 minutes and 20 seconds. [Hint: Use the //
# operator to get minutes and the % operator to get seconds.]


time1 = eval(input("Please enter time in seconds: "))
print(f"Your time is {time1//60} minutes and {time1%60} seconds.")