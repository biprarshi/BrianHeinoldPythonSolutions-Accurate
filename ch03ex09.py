# Write a program that asks the user for an hour between 1 and 12 and for how many hours in
# the future they want to go. Print out what the hour will be that many hours into the future.
# An example is shown below.
# Enter hour: 8
# How many hours ahead? 5
# New hour: 1 o'clock


hour1 = eval(input("Enter hour: "))
hour_add1 = eval(input("How many hours ahead? "))
print("New hour:",(hour1+hour_add1)%12,"o'clock")