#4. Python File Handling & List Comprehension: Write a python program to read contents of a file (filename as argument)
#and store number of occurrences of each word in a dictionary. Display the top 10 words with most number of occurrences 
#in descending order. Store the length of each of these words in a list and display the list. Write a one-line reduce 
#function to get the average length and one-line list comprehension to display squares of all odd numbers and display both.

import sys
import os
from functools import reduce

dict={}

if(len(sys.argv)!=2):
	print("Invalid arguments")
	sys.exit()

if(not(os.path.exists(sys.argv[1]))):
	print("invalid file path")	
	sys.exit()

if(sys.argv[1].split('.')[-1]!="txt"):
	print("invalid File Format. Only TXT files allowed")

with open(sys.argv[1]) as file:
	for line in file:
		for word in line.split():
			dict[word]=dict.get(word,0)+1
	print(dict)

sl=[]
sl=sorted(dict.items(),key=lambda x:x[1],reverse=True)
print(sl[:10])

word=[]
for i,j in sl[:10]:
	word.append(len(i))
print(word)

sum=reduce((lambda x,y:x+y),word)
print("Avg is",sum/len(word))

print([x*x for x in word if x%2!=0])
