#	MSU CSE 231 Spring 2010 Project 5
#	author: Joseph Malandruccolo
#	date:	January 18, 2012
#
#	Program Specs:
#		Prompt the user for a velocity (% of the speed of light)
#		Report the perceived time for astronauts to make the following trips:
#			- Alpha Centauri: 4.3 Light Years
#			- Barnard's Star: 6.0 Light Years
#			- Betelgeuse: 309 Light Years
#			- Andromeda Galaxy: 2,000,000 Light Years


from math import sqrt

#constants
c_M_PER_S = 299792458	#speed of light in meters per second
SHUTTLE_WEIGHT_KG = 70000	#shuttle weigiht in kilograms
#distances in Light Years
DISTANCE_ALPHA_CENTARI = 4.3
DISTANCE_BARNARDS_STAR = 6.0
DISTANCE_BETEGEUSE = 309.0
DISTANCE_ANDROMEDA = 2000000.0
#conversions
VELOCITY_CONVERSION = 3.33564095e-9 #light years per year per meter per second


#factor calculation
def factor(velocity):
	v = (velocity / 100) * c_M_PER_S
	return float(1 / sqrt(1 - (pow(v, 2) / pow(c_M_PER_S,2))))

def time(velocity, distance):
	v = (velocity / 100.0) * c_M_PER_S
	v = v * VELOCITY_CONVERSION
	return float(distance / v)


#prompt the user
bValidInput = False
while not bValidInput:
	try:
		velocity = float(raw_input("Please enter velocity (percentage of the speed of light):\n"))
		if velocity > 0 and velocity < 100:
			bValidInput = True
		else:
			print "Input must be strictly greater than 0 and strictly less than or equal to 100\n"
	except:
		print "Invalid input, please enter a valid floating point number (i.e. 7.0)\n"

#print results
factor = factor(velocity)
print factor
print "At "+str(velocity)+" percent of the speed of light:\n"
print "\tWeight of shuttle:\t"+str(factor * SHUTTLE_WEIGHT_KG)
print "\tPerceived time to travel to Alpha Centauri:\t"+str(time(velocity, DISTANCE_ALPHA_CENTARI) / factor)+" years"
print "\tPerceived time to travel to Barnard's Star:\t"+str(time(velocity, DISTANCE_BARNARDS_STAR) / factor)+" years"
print "\tPerceived time to travel to Betelgeuse:\t"+str(time(velocity, DISTANCE_BETEGEUSE) / factor)+" years"
print "\tPerceived time to travel to Andromeda:\t"+str(time(velocity, DISTANCE_ANDROMEDA) / factor)+" years"