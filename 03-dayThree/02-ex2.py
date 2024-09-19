height = int (input("What is your Height in cm:\n"))
age = int (input("How old are you:\n"))

if height > 120:
    if age <= 12:
        print("Your Ticket will cost $5")
    elif age <=18:
        print("Your Ticket will cost $7") 
    else:
        print("Your Ticket will cost $20")
else:
    print("Sorry you can't ride this Rollercoaster")