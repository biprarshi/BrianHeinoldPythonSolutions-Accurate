# Write a program that asks the user to enter an angle in degrees and prints out the sine of that
# angle.


from math import sin, radians

degrees1 = eval(input("Please enter angle in degrees: "))
radians1 = radians(degrees1)

print("Sine of {}◦ is = {}.".format(degrees1,round(sin(radians1),2)))