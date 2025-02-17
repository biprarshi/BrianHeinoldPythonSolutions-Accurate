# Below is described how to find the date of Easter in any year. Despite its intimidating appear-
# ance, this is not a hard problem. Note that floor(x) is the floor function, which for positive numbers
# just drops the decimal part of the number. For instance floor(3.14) = 3. The floor function is part
# of the math module.

# C = century (1900’s → C = 19)
# Y = year (all four digits)
# m = (15 + C − floor( C/4 ) − floor((8*C+13)/25 )) mod 30
# n = (4 + C − floor( C/4)) mod 7
# a = Y mod 4
# b = Y mod 7
# c = Y mod 19
# d = (19*c + m) mod 30
# e = (2*a + 4*b + 6*d + n) mod 7

# Easter is either March (22 + d + e) or April (d + e − 9). There is an exception if d = 29 and e = 6.
# In this case, Easter falls one week earlier on April 19. There is another exception if d = 28,
# e = 6, and m = 2, 5, 10, 13, 16, 21, 24, or 39. In this case, Easter falls one week earlier on April
# 18. Write a program that asks the user to enter a year and prints out the date of Easter in that
# year. (See Tattersall, Elementary Number Theory in Nine Chapters, 2nd ed., page 167)


from math import floor

Y1 = eval(input('Please enter the year: '))


C1 = Y1//100
m1 = (15 + C1 - floor(C1/4) - floor((8*C1+13)/25)) % 30
n1 = (4 + C1 -floor(C1/4)) % 7
a1 = Y1 % 4
b1 = Y1 % 7
c1 = Y1 % 19
d1 = (19*c1 + m1 )% 30
e1 = (2*a1 + 4*b1 + 6*d1 + n1) % 7


if (d1 == 29) and (e1 == 6):
    print('Easter is on April 19.')
elif (d1 == 28) and (e1 == 6) and (m1 == 2 or m1 == 5 or m1 == 10 or m1 == 13 or m1 == 16 or m1 == 21 or m1 == 24 or m1 == 39):
    print('Easter is on April 18.')
elif (22+d1+e1) < 32:
    print('Easter is on March {}.'.format(22+d1+e1))
elif(d1+e1-9) < 31:
    print('Easter is on April {}.'.format(d1+e1-9))
else:
    print('donno')