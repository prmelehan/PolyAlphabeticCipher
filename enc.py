import math


# A script that creates a Poly Alphabetic Cipher

sentence = input("Gimme your phrase: ")

letters = list(sentence)

#Shift Right Ord
first = letters[0]
first = ord(first)
print(first)
#Shift Left Ord
last = letters[-1]
last = ord(last)
print(last)
ordinated = []
for letter in letters:
	#Converting all letters to their Ordinate Values in ASCII
	ordinatedLetter = ord(letter)
	ordinated.append(ordinatedLetter)
print(ordinated)
#Shift all the numbers by the Ordinated value of the first letter
shiftRightOrdinated = []
for number in ordinated:
	shiftNum = (number + first) % 127
	shiftRightOrdinated.append(shiftNum)
print(shiftRightOrdinated)
shiftLeftOrdinated = []

for number in shiftRightOrdinated:
	shiftNum = (number - last) % 127
	shiftLeftOrdinated.append(shiftNum)
print(shiftLeftOrdinated)
encString = []

for number in shiftLeftOrdinated:
	char = str(chr(number))
	encString.append(char)
print(encString)
print(''.join(encString))
