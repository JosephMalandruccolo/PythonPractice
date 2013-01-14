#
#	MSU CSE 231 Fall 2007 Project 1
#	author: Joseph Malandruccolo
#	date:	January 13, 2013
#
#	Program Specs:
#		Prompt the user for two integers
#		Display the result of each of the following:
#			1) add the first and second numbers
#			2) subtract the second number from the first number
#			3) multiply the first and second numbers
#			4) integer division between first and second numbers and remainder


#prompt the user
print 'Please enter two integers\nAddition, subtraction, multiplication, and division results will be returned'
bValidInput = False
while bValidInput == False:
	try:
		numStr = raw_input('Please enter the first integer\n')
		nVar1 = int(numStr)
		numStr = raw_input('Please enter the second integer\n')
		nVar2 = int(numStr)
		bValidInput = True
	except:
		print 'Invalid input: please enter two valid integers'

#compute 1-4
print "Addition: ",nVar1 + nVar2
print "Subtraction: ",nVar1 - nVar2
print "Multiplication: ", nVar1 * nVar2
if nVar2 == 0:
	print 'Division by 0 is undefined'
else:
	print "Division: ", nVar1 / nVar2, " remainder ", nVar1 % nVar2