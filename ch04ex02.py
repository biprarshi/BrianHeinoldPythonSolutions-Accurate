# Ask the user for a temperature. Then ask them what units, Celsius or Fahrenheit, the temper-
# ature is in. Your program should convert the temperature to the other unit. The conversions
# are F = 9/5 * C + 32 and C = 5/9* (F − 32).


temperature1 = eval(input("Please enter a temperature: "))
units1 = eval(input("What units this temperature is in? Enter 1 for Celsius 2 for Fahrenheit: "))
if units1 == 1:
    temperature2 = 9/5*temperature1 + 32
    print("{} ◦C is {} ◦F.".format(temperature1,temperature2))
elif units1 == 2:
    temperature2 = 5/9*(temperature1-32)
    print("{} ◦F is {} ◦C.".format(temperature1, temperature2))
else:
    print("\aInvalid Input...")