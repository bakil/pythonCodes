# Given your birthday and the current date, calculate your age 
# in days. Compensate for leap days. Assume that the birthday 
# and current date are correct dates (and no time travel). 
# Simply put, if you were born 1 Jan 2012 and todays date is 
# 2 Jan 2012 you are 1 day old.

# IMPORTANT: You don't need to solve the problem yet! 
# Just brainstorm ways you might approach it!

daysOfMonths = [ 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def isLeapYear(year):
	if year % 4 != 0 :
		return False
	else :
		if year % 100 != 0 :
			return True
		else :
		 if year % 400 != 0 :
		 	return False
		 else :
		 	return True

    ##
    # Your code here. Return True or False
    # Pseudo code for this algorithm is found at
    # http://en.wikipedia.org/wiki/Leap_year#Algorithm
    ##
def daysInOneYear(year,month,day):
	tempMonth = 0
	tempDays = 0

	while tempMonth + 1 < month :
		tempDays+= daysOfMonths[tempMonth]
		tempMonth+=1
	tempDays+=day
	if isLeapYear(year) and month > 3 :
		tempDays+=1
	return tempDays


def daysBetweenDates(y1, m1, d1, y2, m2, d2):
    ##
    days = 0
    firstYear = y1
    lastYear = y2

    if firstYear == lastYear :
    	days=days + daysInOneYear(y2,m2,d2) - daysInOneYear(y1,m1,d1) 
    else :
    	days=days + daysInOneYear(y2,m2,d2) - daysInOneYear(y1,m1,d1)
    	while y2-y1 > 0 :
    		if y1 == lastYear :
	    			days+=daysInOneYear(y1,m2,d2)
	    	else :
	    			days+=daysInOneYear(y1,12,31)
	    	y1+=1
	    	
	    ##

	    	
	    

    return days

print daysBetweenDates(1981, 11, 7, 2018, 5, 7)

