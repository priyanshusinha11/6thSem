# electric bill
print("Enter the number of units consumed")
units = int(input())
amt = 0
if units <= 100:
    amt += units * 2.5
elif units <= 200:
    amt += 100 * 2.5 + (units - 100) * 4
else:
    amt += 100 * 2.5 + 100 * 4 + (units - 200) * 5
print("Total bill: ", amt)