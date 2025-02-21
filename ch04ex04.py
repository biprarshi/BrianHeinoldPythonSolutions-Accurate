# Write a program that asks the user how many credits they have taken. If they have taken 23
# or less, print that the student is a freshman. If they have taken between 24 and 53, print that
# they are a sophomore. The range for juniors is 54 to 83, and for seniors it is 84 and over.


credits1 = eval(input("Please enter the no of credits you have taken: "))
if credits1 <= 23:
    print("You are a freshman.")
elif credits1 >= 24 and credits1 <=53:
    print("You are a sophomore.")
elif 54 <= credits1 <= 83:
    print("You are a junior.")
elif 84 <= credits1:
    print("You are a senior.")
else:
    print("Invalid Input!")