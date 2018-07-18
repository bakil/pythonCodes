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
