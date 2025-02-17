# A lot of cell phones have tip calculators. Write one. Ask the user for the price of the meal and
# the percent tip they want to leave. Then print both the tip amount and the total bill with the
# tip included.


print("========Tip Generator========")
price1 = eval(input("Enter price of meal: "))
units1 = eval(input("Enter quantity of meal: "))
total_Price1 = price1 * units1
tip_percent1 = eval(input("Enter percentage tip you want to leave: "))
tip1 = total_Price1 * tip_percent1 / 100
print("Your tip is ",tip1,".",sep="")
print("Total bill with the tip included is ",total_Price1+tip1,".",sep="")
