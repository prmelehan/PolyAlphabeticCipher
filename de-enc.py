import math


# A script that creates a Poly Alphabetic Cipher

sentence = input("Gimme your phrase: ")

letters = list(sentence)

PolyDictA = {'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7,'i':8,'j':9,'k':10,'l':11,'m':12,'n':13,'o':14,'p':15,'q':16,'r':17,'s':18,'t':19,'u':20,'v':21,'w':22,'x':23,'y':24,'z':25, 'A':26, 'B':27,'C':28,'D':29,'E':30,'F':31,'G':32,'H':33,'I':34,'J':35,'K':36,'L':37,'M':38,'N':39,'O':40,'P':41,'Q':42,'R':43,'S':44,'T':45,'U':46,'V':47,'W':48,'X':49,'Y':50,'Z':51,'1':52,'2':53,'3':54,'4':55,'5':56,'6':57,'7':58,'8':59,'9':60,'0':61,'!':62,'@':63,'#':64,'$':65,'%':66,'^':67,'&':68,'*':69,'(':70,')':71,'-':72,'+':73,'=':74,':':75,';':76,'"':77,"'":78,',':79,'<':80,'>':81,'.':82,'?':83,' ':84}
# A function that replaces find_valueA with a custom indexing function for the PolyDictA dictionary

def find_valueA(letter):
	letter = str(letter)
	key = PolyDictA[letter]
	return key
def find_keyA(val):
    for key in PolyDictA.keys():
    	if PolyDictA[key] == val:
    		return str(key)
# Shift Right Ord
first = letters[0]
first = find_valueA(first)
#print(first)
#Shift Left Ord
last = letters[-1]
last = find_valueA(last)
#print(last)
ordinated = []
for letter in letters:
	#Converting all letters to their Ordinate Values in ASCII
	ordinatedLetter = find_valueA(letter)
	ordinated.append(ordinatedLetter)
#print(ordinated)
#Shift all the numbers by the Ordinated value of the first letter
shiftRightOrdinated = []
for number in ordinated:
	shiftNum = (number - first) % 85
	shiftRightOrdinated.append(shiftNum)
#print(shiftRightOrdinated)
shiftLeftOrdinated = []

for number in shiftRightOrdinated:
	shiftNum = (number + last) % 85
	shiftLeftOrdinated.append(shiftNum)
#print(shiftLeftOrdinated)
encString = []

for number in shiftLeftOrdinated:
	char = find_keyA(number)
	encString.append(char)
#print(encString)
print("Output:/" + ''.join(encString))

