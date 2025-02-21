# Write a program that asks the user to enter a length in centimeters. If the user enters a negative
# length, the program should tell the user that the entry is invalid. Otherwise, the program
# should convert the length to inches and print out the result. There are 2.54 centimeters in an
# inch.


length1 = eval(input("Please enter a length in centimeters: "))
if length1 < 0:
    print("The entry is invalid.")
else:
    print("{} centimeters is {} inches.".format(length1, length1/2.54))