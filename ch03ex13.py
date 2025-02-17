# Write a program that asks the user for a number and then prints out the sine, cosine, and
# tangent of that number.


from math import sin, cos, tan

num1 = eval(input("Plese enter your number: "))
print(f"Sine of {num1} =",round(sin(num1),2),end=".\n")
print(f"Cosine of {num1} =",round(cos(num1),2),end=".\n")
print(f"Tangent of {num1} =",round(tan(num1),2),end=".\n")
