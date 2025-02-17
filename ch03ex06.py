# Write a program that asks the user to enter two numbers, x and y , and computes (|x-y|)/(x+ y) .


x1 = eval(input("Please enter first number: "))
y1 = eval(input("Please enter second number: "))

print("(|x-y|)/(x+y) =",abs(x1-y1)/(x1+y1))