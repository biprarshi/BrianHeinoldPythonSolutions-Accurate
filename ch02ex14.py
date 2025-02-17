# Use for loops to print a diamond like the one below. Allow the user to specify how high the
# diamond should be.
#    *         
#   ***        
#  *****       
# *******      
#  *****       
#   ***        
#    *         


height1 = eval(input("Please enter the height of diamond: "))
if height1%2 != 0:
    for i in range(height1//2+1):
        # print(height1-(height1//2+1)-i,1+i*2)
        print(" "*(height1-(height1//2+1)-i)+"*"*(1+i*2))
        
    for i in range(height1//2):
        # print(i+1,height1-2*(i+1))
        print(" "*(i+1)+"*"*(height1-2*(i+1)))
        
else:
    for i in range(height1//2):
        # print(height1//2-i-1,i*2+1)
        print(" "*(height1//2-i-1)+"*"*(i*2+1))
    for i in range(height1//2):
        # print(i,height1-1-2*i)
        print(" "*i+"*"*(height1-1-2*i))
        

