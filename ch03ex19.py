# Write a program that draws “modular rectangles” like the ones below. The user specifies the
# width and height of the rectangle, and the entries start at 0 and increase typewriter fashion
# from left to right and top to bottom, but are all done mod 10. Below are examples of a 3 × 5
# rectangle and a 4 × 8.

# 0 1 2 3 4
# 5 6 7 8 9
# 0 1 2 3 4

# 0 1 2 3 4 5 6 7
# 8 9 0 1 2 3 4 5
# 6 7 8 9 0 1 2 3
# 4 5 6 7 8 9 0 1


height1 = int(input('Please enter modular rectangle height: '))
width1 = int(input('Please enter modular rectangle width: '))

for i in range(height1*width1):
    print(i%10, end=' ')
    if (i+1)%width1 == 0:
        print()

