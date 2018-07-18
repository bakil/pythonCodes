def secondToTime(seconds):
	secondInOneMintus = 60
	secondInOneHour = secondInOneMintus * 60

	hours = seconds/secondInOneHour
	mintes= (seconds%secondInOneHour)/secondInOneMintus
	sec = (seconds%secondInOneHour)%secondInOneMintus

	return str(hours)+":"+str(mintes)+":"+str(sec)
print secondToTime(11165)