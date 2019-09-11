#define a function to convert far to cel
def FarenToCelcius():#defining function
	temp=int(input("please enter the farenheit temprature to convert it into celcius"))#taking input in int
	celcius=(temp-32)*(5/9)#eqution to convert into far
	print("the corresponding celcius temprature is ",celcius)#print result
	return#returns to where it is called
#define a function to convert far to cel
def CelciusToFaren():#defining function
	temp=int(input("please enter the celcius temprature to convert it into Farenheit"))#taking input in int
	faren=(9/5)*(temp)+32#eqution to convert into cel
	print("the corresponding celcius temprature is ",faren)#print result
	return#returns to where it is called

m=1
while(m==1):
	print (" welcome to temprature conversion system ")
	print ("MENU")
	print ("1.Farenheit to celcius ")
	print ("2.celcius to farenheit ")
	choice=int(input("choose from the following options"))#taking input for choice
	if(choice==1):
		FarenToCelcius()#function call
	elif(choice==2):
		CelciusToFaren()#function call
	else:
		print ("you have entered a wrong input ")
	m=int(input("press 1 if you want to do some more conversions or press 0 to exit "))#taking input to continue or exit
	
	#Farenheit to celcius 
	#celcius=(temp-32)*(5/9)

	#Farenheit to kelvin
	#kelvin=(temp-32)*(5/9)+273

	#celcius to kelvin
	#kelvin=temp+273

	#celcius to farenheit
	#faren=(9/5)*(temp)+32

	#kelvin to farenheit
	#faren=(9/5)*(temp+273)+32

	#kelvin to celcius
	#celcius=(temp-273)
	
