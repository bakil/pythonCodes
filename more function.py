# 1- code to convert from second to HH:MM:SS
# 2- make a rectangle box around text
# 3- circle area


""" 1- code to convert from second to HH:MM:SS """
def secondToTime(seconds):
	secondInOneMintus = 60
	secondInOneHour = secondInOneMintus * 60

	hours = seconds/secondInOneHour
	mintes= (seconds%secondInOneHour)/secondInOneMintus
	sec = (seconds%secondInOneHour)%secondInOneMintus

	return str(hours)+":"+str(mintes)+":"+str(sec)
print secondToTime(65)


""" 2- make a rectangle box around text """
def bar(n,ch="-"):
	return n * ch
def box(text):
	print "+" + bar(len(text)) + "+"
	print "|" + text + "|"
	print "+" + bar(len(text)) + "+"

box("How are you")


""" 3- circle area """
def area():
	x= input("enter X ")
	y= input("enter y ")
	return x*y
print area()
