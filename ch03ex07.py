# Write a program that asks the user to enter an angle between −180◦ and 180◦ . Using an
# expression with the modulo operator, convert the angle to its equivalent between 0◦ and
# 360◦ .


angle1 = eval(input("Please enter an angle between −180◦ and 180◦ : "))
if (angle1 >= -180) and (angle1 <= 0):
    print(f"Your angle is: {angle1%360}◦.")
elif (angle1 >= 0) and (angle1 <= 180):
    print(f"Your angle is: {angle1}◦.")
else:
    print("Invalid input!") 
