#  1-  Break Time, webbrowser, time
import webbrowser
import time

listOfYouTubeURL = ["G:\\new ibb\\music\\1.mp4","G:\\new ibb\\music\\2.mp4","G:\\new ibb\\music\\3.mp4"]
print "this code start at " ,  time.ctime() 
for url in listOfYouTubeURL :
	time.sleep(2*5)
	webbrowser.open(url,new=1)


# class
class Parent():
	def __init__(self,last_name,eye_color):
		print("Parent constructor called")
		self.last_name = last_name
		self.eye_color = eye_color
	def show_info(self):
		print "parent info : ", self.last_name , self.eye_color

class Child(Parent): # this mean class child will inhert class Parent
	def __init__(self,last_name,eye_color,number_of_toys): 
		print "child constructor called"
		Parent.__init__(self,last_name,eye_color)# here we initilize parent class from child class
		self.number_of_toys = number_of_toys
	def show_info(self): 
	# when child and parent have same method name ==> method override
		print "child info : ", self.last_name , self.eye_color ,self.number_of_toys


miley_cyrus = Child("Cyrus","blue",5)
print miley_cyrus.last_name
print miley_cyrus.number_of_toys

miley_cyrus.show_info()


# profanity check
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






#  remove numbers from text
def remove_number(text):
    text_without_no = '' #empty string for now
    while text != '':
        next_character = text[0]
        if next_character not in '0123456789':    #that's a single space
            text_without_no = text_without_no + next_character
        text = text[1:]
    return text_without_no
print remove_number("hello 145321 my name is andy how are you?")








# rename files in folder
import os
def rename_files():
	#(1) get files names from a folder
	file_list = os.listdir(r"C:\Python27\code\family")
	# list all file inside folder to a list object
	# we add r to tell os juse take path as it is. note: work without
	#(2) to save current path to var
	saved_path = os.getcwd() # return current location of python file
	print("Current working directory is " + saved_path)
	#(3) change working directory to the same folder of photos
	os.chdir(r"C:\Python27\code\family") # change working directory

	for file_name in file_list :
		print "old name - " + file_name
		new_name = file_name.translate(None,"0123456789")
		# transilate here will remove any number in file name
		print "new name - " + new_name
		os.rename(file_name,new_name) # rename files in current dir with new name

	#(6) return system to old path
	os.chdir(saved_path)

rename_files()





# twilio
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC791f622a0067edc458dfd31c090f48b8"
# Your Auth Token from twilio.com/console
auth_token  = "240511aea1e6dcd9b162cb95b917f428"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+601162319354", #your phone number
    from_="+17479008179", # twilio phone no
    body="Hello from Python!")

print(message.sid)








# transilate function

from string import maketrans   # Required to call maketrans function.

intab = "aeiou"
outtab = "12345"
trantab = maketrans(intab, outtab) # use it to create transilation
str = "this is string example....wow!!!";
print str.translate(trantab) ##  th3s 3s str3ng 2x1mpl2....w4w!!!

a = "How are you"
b=a.translate(None,"o") ## here we don't use table transilate but we delete char o
print b ## Hw are yu




