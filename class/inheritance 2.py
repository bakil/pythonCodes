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

