# A store charges $12 per item if you buy less than 10 items. If you buy between 10 and 99
# items, the cost is $10 per item. If you buy 100 or more items, the cost is $7 per item. Write a
# program that asks the user how many items they are buying and prints the total cost.

no_items1 = eval(input("Please enter the no of items that you are buying: "))
if no_items1 < 10:
    total_cost1 = no_items1 * 12
elif no_items1 < 100:
    total_cost1 = no_items1 * 10
elif no_items1 > 99:
    total_cost1 = no_items1 * 7

print("Total cost is: $",total_cost1,sep="")