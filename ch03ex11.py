# Write a program that asks the user to enter a weight in kilograms. The program should
# convert it to pounds, printing the answer rounded to the nearest tenth of a pound.


w_kg1 = eval(input("Please enter your weight in kg: "))
w_pound1 = w_kg1*2.2046226218487758848
print(f"{w_kg1} kgs is {round(w_pound1,1)} pounds.")
