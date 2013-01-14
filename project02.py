#
#	MSU CSE 231 Fall 2008 Project 2
#	author: Joseph Malandruccolo
#	date:	January 13, 2013
#
#	Program Specs:
#		Prompt the user for the number of gallons of gasoline purchased
#		Report summary information including:
#			1) the number of liters
#			2) the number of barrels of gasoline
#			2) the number of barrels of oil required
#			3) the pounds of CO2 produced
#			4) equivalent energy amount of ethanol gallons
#			5) the cost in US dollars


#constants
LITERS_PER_GALLON = 3.78541
BARRELS_PER_GALLON = 0.0238095238
PERCENT_GASOLINE_IN_OIL_BARREL = 19.5 / 42.0
CO2_LBS_PER_GALLON = 20
BTU_PER_GALLON_GAS = 115000
BTU_PER_GALLON_ETHANOL = 75700
#Chicago's average price per gallon of gasoline in 2012
AVERAGE_PRICE_PER_GAS_GALLON = 3.851


#prompt the user
bValidInput = False
while bValidInput == False:
	try:
		gallons = float(raw_input('Please input the number of gallons of gasoline purchased:\n'))
		bValidInput = True
	except:
		print 'Invalid input, please enter a floating point number (e.g. 7.2)'


#print results
print 'Number of Gallons: ' + str("%.2f" % gallons)
print 'Liters:\t' + str("%.2f" % (gallons * LITERS_PER_GALLON))
print 'Barrels of Gasoline:\t' + str("%.2f" % (gallons * BARRELS_PER_GALLON * PERCENT_GASOLINE_IN_OIL_BARREL))
print 'Barrels of Oil Required:\t' + str("%.2f" % (gallons * BARRELS_PER_GALLON))
print 'Pounds of CO2 Produced:\t' + str("%.2f" % (gallons * CO2_LBS_PER_GALLON))
print 'Equivalent Gallons of Ethanol:\t' + str("%.2f" % (gallons * BTU_PER_GALLON_GAS / BTU_PER_GALLON_ETHANOL))
print 'Cost (2012 dollars):\t$' + str("%.2f" % (gallons * AVERAGE_PRICE_PER_GAS_GALLON))