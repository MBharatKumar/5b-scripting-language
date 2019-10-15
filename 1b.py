#b) Write a python program to count the frequency of words in a given file. 

import sys,os

dict = {}
wordLen = []

if(len(sys.argv) != 2):
	print ("Invalid Arguments")
	sys.exit()

if(not(os.path.exists(sys.argv[0]))):
	print ("Invalid File Path")
	sys.exit()

if(sys.argv[1].split('.')[-1] != "txt"):
	print ("Invalid File Format. Only TXT files allowed")
	sys.exit()

with open(sys.argv[1]) as file:
	content=file.read()
	mylist=content.split()
	mydict=dict.fromkeys(mylist)
	#print(mydict)
	olist=list(mydict)
	for i in range(len(olist)):
    		print("Frequency of ",olist[i]," : ",mylist.count(olist[i]))
