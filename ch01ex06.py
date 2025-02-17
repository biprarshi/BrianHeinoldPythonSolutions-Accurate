# Ask the user to enter a number x . Use the sep optional argument to print out x , 2x , 3x , 4x ,
# and 5x , each separated by three dashes, like below.
# Enter a number: 7
# 7---14---21---28---35


num1 = eval(input("Enter a number: "))
print(num1,num1*2,num1*3,num1*4,num1*5,sep="---")