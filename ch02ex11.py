# Use a for loop to print a box like the one below. Allow the user to specify how wide and how
# high the box should be.
# ********************
# *                  *
# *                  *
# ********************

width1 = eval(input("Please enter width of box: "))
height1 = eval(input("Please enter height of box: "))
print("*"*width1)
for i in range(height1-2):
    print("*"+" "*(width1-2)+"*")
print("*"*width1)