# (a) One way to find out the last digit of a number is to mod the number by 10. Write a
# program that asks the user to enter a power. Then find the last digit of 2 raised to that
# power.
# (b) One way to find out the last two digits of a number is to mod the number by 100. Write
# a program that asks the user to enter a power. Then find the last two digits of 2 raised to
# that power.
# (c) Write a program that asks the user to enter a power and how many digits they want.
# Find the last that many digits of 2 raised to the power the user entered.


num_power1 = eval(input("Please enter a power: "))

print('(a)')
print(f"The last digit of 2**{num_power1} =",(2**num_power1)%10)
print('(b)')
print(f'The last two digits of 2**{num_power1} =',(2**num_power1)%100)

print('(c)')
number1 = 2**num_power1
no_digits1 = eval(input("Please enter the no of digits you want: "))
last_n_digits1 =  number1%(10**no_digits1)
if (len(str(last_n_digits1)) < no_digits1) and (len(str(number1))>no_digits1):
    last_n_digits1 = '0'*(no_digits1-len(str(last_n_digits1)))+str(last_n_digits1)



print(f'The last {no_digits1} digits of 2**{num_power1} =',last_n_digits1)
