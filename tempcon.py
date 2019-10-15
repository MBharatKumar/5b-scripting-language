#2. Introduction to Python Functions: Write a temperature converter python program, which is menu driven. Each such conversion
#logic should be defined in separate functions. The program should call the respective function based on the user‟s requirement.
#The program should run as long as the user wishes so. Provide an option to view the conversions stored as list of tuples with 
#attributes - from unit value, to unit value sorted by the user‟s choice (from-value or to-value). 

def FarenToCelcius():
	temp=int(input("please enter the farenheit temprature to convert it into celcius"))
	celcius=(temp-32)*(5/9)
	print("the corresponding celcius temprature is ",celcius)
	return

def CelciusToFaren():
	temp=int(input("please enter the celcius temprature to convert it into Farenheit"))
	faren=(9/5)*(temp)+32
	print("the corresponding celcius temprature is ",faren)
	return

m=1
while(m==1):
	print (" welcome to temprature conversion system ")
	print ("MENU")
	print ("1.Farenheit to celcius ")
	print ("2.celcius to farenheit ")
	choice=int(input("choose from the following options"))
	if(choice==1):
		FarenToCelcius()
	elif(choice==2):
		CelciusToFaren()
	else:
		print ("you have entered a wrong input ")
	m=int(input("press 1 if you want to do some more conversions or press 0 to exit "))
	
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
	
