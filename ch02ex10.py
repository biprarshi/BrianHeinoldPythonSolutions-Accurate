# Use a for loop to print a box like the one below. Allow the user to specify how wide and how
# high the box should be. [Hint: print('*'*10) prints ten asterisks.]
# *******************
# *******************
# *******************
# *******************


width1 = eval(input("Please enter box width: "))
height1 = eval(input("Please enter box height: "))

for i in range(1,height1+1):
    print("*  "*width1)