from time import mktime 
from datetime import datetime
def parseDate(y,m,d):
    return mktime(datetime.strptime("{}/{}/{}".format(y,m,d),"%Y/%m/%d").timetuple())
def toDays(seconds):
    return int(abs(seconds/60/60//24))
def daysBetweenDates(y1,m1,d1,y2,m2,d2):
    return toDays(parseDate(y2,m2,d2)) - toDays(parseDate(y1,m1,d1)) 

print daysBetweenDates(2012,12,2,2012,12,5)