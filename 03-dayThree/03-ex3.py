weight = float(input("What is your Weight in kgs:\n"))
height = float(input("What is your Height in m:\n"))

BMI = round((float (weight/(height ** 2) )) , 2)
print(f"Your BMI is {BMI}")

if BMI < 18.5:
    print("You are uderweight")
elif BMI < 25:
    print("You have normal weight")
elif BMI < 30:
    print("You are Overweight")
elif BMI < 35:
    print("You are Obese")
else:
    print("You are clinically Obese")