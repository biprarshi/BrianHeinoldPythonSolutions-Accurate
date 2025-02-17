# Write a program that prints out a list of the integers from 1 to 20 and their squares. The output
# should look like this:
# 1 --- 1
# 2 --- 4
# 3 --- 9
# ...
# 20 --- 400


for i in range(20):
    print(i+1,"---",(i+1)*(i+1))