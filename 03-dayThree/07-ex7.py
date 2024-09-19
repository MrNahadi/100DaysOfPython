name1 =str( input("what is your name:\n"))
name1 = name1.lower()
name2 = str(input("what is their name:\n"))
name2 = name2.lower()
combined = name1+name2
n = len(combined)

t = int(combined.count("t", 0 , n))
r = int(combined.count("r", 0 , n))
u = int(combined.count("u", 0 , n))
e = int(combined.count("e",0 ,n))
number1 = t+r+u+e
number1 = str(number1)

l = int (combined.count("l",0,n))
o = int(combined.count("o",0,n))
v = int(combined.count("v",0,n))
e2 = int(combined.count("e",0,n))
number2 = l+o+v+e2
number2 =str(number2)

score = number1+number2
scoreNum = int (score)

if scoreNum>40 and scoreNum<50:
    print(f"Your Score is {scoreNum} you are alright together")
else:
    print(f"Your Score is {scoreNum}")