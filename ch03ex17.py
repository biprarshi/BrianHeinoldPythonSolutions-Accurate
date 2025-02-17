# A year is a leap year if it is divisible by 4, except that years divisible by 100 are not leap years
# unless they are also divisible by 400. Ask the user to enter a year, and, using the // operator,
# determine how many leap years there have been between 1600 and that year.


year1 = eval(input('Enter year: '))
count_leap1 = 0

for i in range(1600, year1+1):
    if (i%4 == 0) and (i%100 != 0):
        count_leap1+=1
        print(i)
    elif (i%400 == 0):
        count_leap1+=1
        print(i)

print(f'No of leap years between 1600 and {year1} is {count_leap1}.')