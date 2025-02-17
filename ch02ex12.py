# Use a for loop to print a triangle like the one below. Allow the user to specify how high the
# triangle should be.
# *
# **
# ***
# ****


height1 = eval(input("Please enter the height of triangle: "))

for i in range(height1):
    print("*"*(i+1))