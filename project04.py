#	MSU CSE 231 Fall 2009 Project 4
#	author: Joseph Malandruccolo
#	date:	January 13, 2013
#
#	Program Specs:
#		Prompt the user for a year
#		Report the U.S. population
#			- actual if in the past
#			- projected if in the future

#constants
US_POPULATION_2013 = 315163513
SECONDS_BETWEEN_BIRTHS = 8
SECONDS_BETWEEN_DEATHS = 12
SECONDS_BETWEEN_NET_IMMIGRANT = 40
SECONDS_PER_MINUTE = 60
MINUTES_PER_HOUR = 60
HOURS_PER_DAY = 24
DAYS_PER_YEAR = 365.242


#compute population change per year
birthsPerMin = float(SECONDS_PER_MINUTE) / SECONDS_BETWEEN_BIRTHS
deathsPerMin = float(SECONDS_PER_MINUTE) / SECONDS_BETWEEN_DEATHS
immigrationPerMin = float(SECONDS_PER_MINUTE) / SECONDS_BETWEEN_NET_IMMIGRANT
netPopulationChangePerMin = birthsPerMin + immigrationPerMin - deathsPerMin
netPopulationChangePerYear = netPopulationChangePerMin * MINUTES_PER_HOUR * HOURS_PER_DAY * DAYS_PER_YEAR

#prompt the user for a year
print "Welcome to the American Console Population Estimator!"
bValidInput = False
while bValidInput == False:
	try:
		years = int(raw_input("How many years in the future would you like to see data for?\n"))
		if years > 0:
			bValidInput = True
		else:
			print "Year must be a positive integer (e.g. 4)"
	except:
		print "Year must be a positive integer (e.g. 4)"

#print results
print "2013 US Population:\t" + str(US_POPULATION_2013)
print "Estimated growth over " + str(years) + "years:\t" + str(netPopulationChangePerYear * years)
print str(2013 + years) + " US Population (Est)\t" + str(US_POPULATION_2013 + netPopulationChangePerYear * years)