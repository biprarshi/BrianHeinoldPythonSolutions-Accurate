# A year is a leap year if it is divisible by 4, except that years divisible by 100 are not leap years
# unless they are also divisible by 400. Write a program that asks the user for a year and prints
# out whether it is a leap year or not.


year1 =- eval(input('Pleasse enter year: '))
if(year1%4 == 0 and year1%100 !=0) or (year1%400 == 0):
    print("It's a leap year.")
else:
    print("It's not a leap year.")