#import system for Python version check
import sys

#Check to see if python version is version 3

if(sys.version_info[0] < 3):
	exit("Python 3 is required")

# A script that creates a Poly Alphabetic Cipher

sentence = input("Gimme your phrase: ")
shiftword = input("Provide shift word: ")

#Seperates each letter as own index in array
shiftletters = list(shiftword)
#Same as above comment____________^^
letters = list(sentence)
PolyDict = {'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7,'i':8,'j':9,'k':10,'l':11,'m':12,'n':13,'o':14,'p':15,'q':16,'r':17,'s':18,'t':19,'u':20,'v':21,'w':22,'x':23,'y':24,'z':25, 'A':26, 'B':27,'C':28,'D':29,'E':30,'F':31,'G':32,'H':33,'I':34,'J':35,'K':36,'L':37,'M':38,'N':39,'O':40,'P':41,'Q':42,'R':43,'S':44,'T':45,'U':46,'V':47,'W':48,'X':49,'Y':50,'Z':51,'1':52,'2':53,'3':54,'4':55,'5':56,'6':57,'7':58,'8':59,'9':60,'0':61,'!':62,'@':63,'#':64,'$':65,'%':66,'^':67,'&':68,'*':69,'(':70,')':71,'-':72,'+':73,'=':74,':':75,';':76,'"':77,"'":78,',':79,'<':80,'>':81,'.':82,'?':83,' ':84}
#Checks to see if there was even input
if(len(shiftletters) == 0 or len(sentence) == 0):
	exit("Both a passphrase and a phrase to be encoded is required")

#create a check to see if the input is in the dictionary
notInDictErrorMsg = "Invalid Chracters: One or more characters in your phrase or passcode is not accepted by this program"
#Check the phrase for valid characters
for letter in sentence:
	if(letter in PolyDict):
		pass
	else:
		exit(notInDictErrorMsg)
#Check the passcode for valid chracters
for letter in shiftword:
	if(letter in PolyDict):
		pass
	else:
		exit(notInDictErrorMsg)
##end check for dictionary
#print(letters)
# A function that replaces ord() with a custom indexing function for the PolyDict dictionary

def find_value(letter):
	letter = str(letter)
	key = PolyDict[letter]
	return key
def find_key(val):
    for key in PolyDict.keys():
    	if PolyDict[key] == val:
    		return str(key)
ordinated = []
for letter in letters:
	#Converting all letters to their PolyDict equivilants
	ordinatedLetter = find_value(letter)
	ordinated.append(ordinatedLetter)
#print(ordinated)
#Shift all the numbers by the "Ordinated" value of the first letter

encString = []
#Use the shift word to shift the characters
usedChars = []
allshifted = []
#Shift based on word
for number in ordinated:
	#Get first letter in shift word array]
	#First check to see if it is empty
	if(len(shiftletters) > 0):
		shiftLetter = shiftletters[0]
		#print("Shift Letter: " + shiftLetter)
		convertedLetter = find_value(shiftLetter)
		#print("Converted Shift Letter: ", convertedLetter)
		shiftByNum = (number + convertedLetter) % 85

		allshifted.append(shiftByNum)
		usedChars.append(shiftLetter)
		del shiftletters[0]
		if(len(shiftletters) == 0):
			for element in usedChars:
				shiftletters.append(element)
			del usedChars[:]
		#print("Used Characters: ", usedChars, "Usable Characters: ", shiftletters)
	elif(len(shiftletters) == 0):
		for element in usedChars:
			shiftletters.append(element)
		del usedChars[:]
#print(allshifted)
for number in allshifted:
	char = find_key(number)
	encString.append(char)
#print(encString)
print(''.join(encString))
