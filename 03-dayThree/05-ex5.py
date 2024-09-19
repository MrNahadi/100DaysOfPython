height = int(input("what is your height\n"))
age = int(input("How old are you\n"))
bill = 0

if height >= 120:
    if age > 45 and age < 55:
        print("You can ride for free")
    else:
        if age < 12:
            bill +=5
            print("Kids tickets are $5")
        elif age <= 18:
            bill +=7
            print("Teen Tickets are $7")
        else:
            bill +=10
            print("Adult Tickets are $10")
    
        photo = input("Do you want a photo: Y or N\n")
        if photo == "Y":
            bill +=3
            print(f"your bill is ${bill}")
        else:
            print (f"Your bill is $ {bill}")
else:
    print("You are too short for this ride")