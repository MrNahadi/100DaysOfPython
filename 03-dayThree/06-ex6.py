size = input("What Pizza size do you want: Small(S)/Medium(M)/Large(L):\n")
Bill = 0

if size == "S":
    Bill+= 15
    print(f"The Small Pizza is ${Bill}")
elif size == "M":
    Bill+=20
    print(f"The Medium Pizza is ${Bill}")
else:
    Bill +=25
    print(f"The Large Pizza is ${Bill}")

pepperoni = input("Would you like Pepperoni with that? Y or N\n")
 
if size == "S":
    Bill+=2
    if pepperoni == "Y":
        print(f"Your current Bill is ${Bill}")
    else:
        print(f"Your current  Bill is ${Bill}")
else:
    if pepperoni == "Y":
        Bill += 3
        print(f"Your current Bill is ${Bill}")
    else:
        print(f"Your current Bill is {Bill}")

cheese = input("Would you like some extra cheese with that: Y or N\n")

if cheese == "Y":
    Bill +=1
    print (f"Your bill is ${Bill}")
else:
    print(f"Your bill is {Bill}")
