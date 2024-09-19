# Tip Calculator 

bill = float (input("What is your bill\n"))
tipPercentage = int(input("What percentage would you like to tip\n"))
tip = (tipPercentage/100) * bill
totalBill = bill + tip
splits = int(input("How many people will be splitting ths bill\n"))
split = round(totalBill / splits, 2)

print (f"Your split is {split}")


