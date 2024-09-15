# come up wit a program that gets 2 values from the user, saves then in a variable and swaps the two values 
# i.e say a= 1 and b =2 swap a to be 2 and b to be 1

a = int(input('a: '))
b = int (input('b: '))

c = a
a = b
b = c

print('a:',a)
print('b:',b)

#BONUS Come up with the program without introducing a third variable(c)

a,b = b,a

print('a:', a)
print('b:',b)