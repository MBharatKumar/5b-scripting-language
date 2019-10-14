#3. Python Classes: Write a python class to reverse a sentence (initialized via constructor) word by word.
#Example: “I am here” should be reversed as “here am I”. Create instances of this class for each of the three 
#strings input by the user and display the reversed string for each, in descending order of number of vowels in the string.

class SentenceReverser:
	vowels = ["a","e","i","o","u"]
	sentence = ""
	reverse = ""
	vowelCount = 0
	def __init__(self,sentence):
		self.sentence = sentence
		self.reverseSentence()
	def reverseSentence(self):
		self.reverse = " ".join(reversed(self.sentence.split()))
	def getVowelCount(self):
		self.vowelCount = sum(s in self.vowels for s in self.sentence.lower())
		return self.vowelCount
	def getReverse(self):
		return self.reverse

items = []

for i in range(3):
	reverser = SentenceReverser(raw_input("Enter a sentence :"))
	items.append(reverser)
	print(reverser.reverse)

print ("Sorted descending vovel count: ")
for i in sorted(items,key=lambda item:item.getVowelCount(),reverse=True):
	print (i.getReverse(),"->",i.getVowelCount())

