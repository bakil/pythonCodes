import urllib
def read_text():
	quotes = open("text.txt");
	contents_of_file = quotes.read();
	#print contents_of_file
	quotes.close()
	check_profanity(contents_of_file)

def check_profanity(text_to_check):
	#connection = urllib.urlopen("https://www.purgomalum.com/service/containsprofanity?text=" + text_to_check)
	connection = urllib.urlopen(" http://www.wdylike.appspot.com/?q=" + text_to_check)
	output = connection.read()
	#print output
	if "true" in output:
		print "profanity alert"
	elif "false" in output:
		print "clear from profanity"
	else :
		print " could not check the document properly"


	connection.close()

read_text()
