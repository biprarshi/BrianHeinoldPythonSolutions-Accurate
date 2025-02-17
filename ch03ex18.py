# Write a program that given an amount of change less than $1.00 will print out exactly how
# many quarters, dimes, nickels, and pennies will be needed to efficiently make that change.
# [Hint: the // operator may be useful.]


change_amt1 = eval(input('Please enter amount in cents (1-99): '))

temp1 = change_amt1
quarters1 = temp1 // 25
temp1 = temp1 % 25
dimes1 = temp1 // 10
temp1 = temp1 % 10
nickels1 = temp1 // 4
pennies1 = temp1 % 4

print(f'{change_amt1} cents is {quarters1} quarters, {dimes1} dimes, {nickels1} nickeles and {pennies1} pennies.')