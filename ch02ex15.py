# Write a program that prints a giant letter A like the one below. Allow the user to specify how
# large the letter should be.

#     *
#    * *
#   *****
#  *     *
# *       *

size1 = eval(input("Please enter the size of letter \'A\': "))

print(" "*(size1-1)+"*")
if size1%2 != 0:
    for i in range(size1-1):
        if i != size1//2-1:
            print(" "*(size1-2-i)+"*"+" "*(i*2+1)+"*")
            # print((size1-i-2),(i*2+1))
        else:
            print(" "*(size1//2)+"*"*size1)
            # print((size1//2),size1)
else:
    for i in range(size1-1):
        if i+1 != size1//2:
            print(" "*(size1-2-i)+"*"+" "*(i*2+1)+"*")
        else:
            print(" "*(size1//2-1)+"*"*(size1+1))
            
