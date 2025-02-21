# Write a program that asks the user for an hour between 1 and 12, asks them to enter am or pm,
# and asks them how many hours into the future they want to go. Print out what the hour will
# be that many hours into the future, printing am or pm as appropriate. An example is shown
# below.
# Enter hour: 8
# am (1) or pm (2)? 1
# How many hours ahead? 5
# New hour: 1 pm


hour1 = eval(input('Enter hour: '))
tap1 = eval(input('am (1) or pm (2)? '))
tap2 = 'am' if tap1 == 1 else 'pm'
h_ahead1 = eval(input('How many hours ahead? '))
print('New hour:',hour1+h_ahead1 if hour1+h_ahead1 < 12 else (hour1+h_ahead1)%12, end = ' ')
print(tap2 if hour1+h_ahead1 < 12 else 'am' if tap2 == 'pm' else 'pm' )