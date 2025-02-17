# Write a program to fill the screen horizontally and vertically with your name. [Hint: add the
# option end='' into the print function to fill the screen horizontally.]


name1 = input("Please enter your name: ")
repetition1 = eval(input("Please enter the no of times to repeat: "))
for i in range(repetition1):
    print(name1,end="")

print()

#  print(name1*repetition1)