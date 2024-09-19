# There are various types of data in programming
# They are basically 'types/forms of data' ie that variables can exist as
# They include Strings(letters/words), integers(whole numbers) ,float(decimal numbers) and booleans (True/False) 

numChar = len(input('What is your name?: \n'))

print(type(numChar))

newNum = str(numChar)

print('Your name has '+ newNum +' characters')

print('Your name has ' , numChar , 'characters')