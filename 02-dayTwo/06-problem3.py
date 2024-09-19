# If you are to live to 90 years come up with a program that can get you time left in months weeks and days

age = int(input("How old are you: \n"))
timeLeft = 90 - age

months = timeLeft * 12
weeks = timeLeft  *  52
days = timeLeft * 365

print(f"You have {days} days ,{weeks} weeks, {months} months left")

