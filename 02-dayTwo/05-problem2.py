# BMI calculator

weight = float (input("What is your WEIGHTS in KG: \n"))
height = float (input("What is your HEIGHT in M\n"))

bmi = int (weight/(height**2))

print(f"Your BMI is {bmi} kg/m^2")