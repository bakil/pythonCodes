# Given your birthday and the current date, calculate your age 
# in days. Compensate for leap days. Assume that the birthday 
# and current date are correct dates (and no time travel). 
# Simply put, if you were born 1 Jan 2012 and todays date is 
# 2 Jan 2012 you are 1 day old.

# IMPORTANT: You don't need to solve the problem yet! 
# Just brainstorm ways you might approach it!

daysOfMonths = [ 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
daysOfMonthsInLeapYear = [ 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]



def isLeapYear(year):
	if year % 4 != 0 :
		return False
	elif year % 100 != 0 :
		return True
	elif year % 400 != 0 :
		return False
	else :
		return True



def daysInFullMonth(tempYear,tempMonth):
	if isLeapYear(tempYear):
		return daysOfMonthsInLeapYear[tempMonth-1]
	else :
		return daysOfMonths[tempMonth-1]

def daysInFullYear(tempYear):
	if isLeapYear(tempYear):
		return 366
	else :
		return 365

def daysInPartOfYear(y,m,d):
	days=d
	for month in range(1,m):
		days+=daysInFullMonth(y,month)
	return days

	

def dateValidate(y1,m1,d1,y2,m2,d2):
	if y1*365+m1*30+d1 > y2*365+m2*30+d2:
		return "second date should be after first date"
	elif m1 not in [1,2,3,4,5,6,7,8,9,10,11,12] or m2 not in [1,2,3,4,5,6,7,8,9,10,11,12] :
		return "month value not accepted"
	elif d1<1 or d1> daysInFullMonth(y1,m1) :
		return "day in first date is not accepted"
	elif d2<1 or d2> daysInFullMonth(y2,m2) :
		return "day in Second date is not accepted"
	else :
		return "pass"


def daysBetweenDates(y1, m1, d1, y2, m2, d2):
    ## first check if inputs are valid
    validDate = dateValidate(y1,m1,d1,y2,m2,d2)
    if validDate != "pass" :
    	return validDate

    days = 0
    firstYear = y1
    lastYear = y2
    while y2 > y1 + 1 :
    	days+=daysInFullYear(y1+1)
    	y1+=1

    if lastYear>firstYear :
    	days+=daysInPartOfYear(lastYear,m2,d2)
    	days+=daysInFullYear(firstYear)-daysInPartOfYear(firstYear,m1,d1)
    else :
    	days+=daysInPartOfYear(lastYear,m2,d2)-daysInPartOfYear(firstYear,m1,d1)

    return days


def test():
    test_cases = [((2012,9,30,2012,10,30),30), 
                  ((2012,1,1,2013,1,1),366),
                  ((2012,9,1,2012,9,4),3)]
    
    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print "Test with data:", args, "failed" , result
        else:
            print "Test case passed!"

def myTest():
    assert isLeapYear(2000)
    assert daysInFullMonth(2000,2)==29
    assert daysInFullMonth(2001,2)==28 , "not a leap yrar"
    assert daysInFullYear(2000)==366
    assert daysInFullYear(2001)==365
    assert daysInPartOfYear(2000,1,15)==15
    assert daysInPartOfYear(2000,3,1)==61
    assert daysInPartOfYear(2001,3,1)==60
    assert daysBetweenDates(2012,9,30,2012,10,30)==30
    assert daysBetweenDates(2012,1,1,2013,1,1)==366
    assert daysBetweenDates(2012,9,1,2012,9,4)==3
    print "myTest finish"

def main():
    test()
    myTest()
    print daysBetweenDates(2012,9,1,2012,9,1)
if __name__ == "__main__":
  main()    	

    	
