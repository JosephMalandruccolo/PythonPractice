#	MSU CSE 231 Spring 2008 Project 3
#	author: Joseph Malandruccolo
#	date:	January 13, 2013
#
#	Program Specs:
#		Prompt the user for a floating point value representing miles/hour
#		Report summary information including:
#			1) barleycorns/day
#			2) furlongs/fortnight
#			3) Mach number
#			4) percentage of the speed of light


#constants
#time
HOURS_PER_DAY = 24.0
DAYS_PER_FORTNIGHT = 14.0
MINUTES_PER_HOUR = 60.0
SECONDS_PER_MINUTE = 66.0

#distance
YARDS_PER_FURLONG = 220.0
FEET_PER_YARD = 3.0
BARLEYCORNS_PER_MILE = 189334.588235
FEET_PER_METER = 3.28084
METERS_PER_MILE = 1609.34
FURLONGS_PER_MILE = 8.0

#speed
MACH1_FEET_PER_SECOND = 1116.0
C_METERS_PER_SECOND = 299792458.0

#prompt the user
while True:
	try:
		milesPerHour = float(raw_input("Please enter a speed in miles/hr:\n"))
		break;
	except:
		print 'Invalid entry; please enter a floating point value (i.e. 34.21)'

#print the results, converting miles/hr to distance/hr then distance/time
print 'Barleycorns per day:\t' + str((milesPerHour * BARLEYCORNS_PER_MILE) * HOURS_PER_DAY)
print 'Furlongs per fortnight:\t' + str((milesPerHour * FURLONGS_PER_MILE) * HOURS_PER_DAY * DAYS_PER_FORTNIGHT)
print 'Mach:\t' + str(((milesPerHour * METERS_PER_MILE * FEET_PER_METER) / MINUTES_PER_HOUR / SECONDS_PER_MINUTE) / MACH1_FEET_PER_SECOND)
print 'Percent of the Speed of Light\t' + str(((milesPerHour * METERS_PER_MILE) / MINUTES_PER_HOUR / SECONDS_PER_MINUTE) / C_METERS_PER_SECOND)