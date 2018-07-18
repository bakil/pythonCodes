import webbrowser

class Movie(): # it is better to capitalize first letter of class name
	""" this is document for this class, any thing between three qutation will be saved to a class variable doc """
	COMMON_VARIABLE = "any variable under the class directly, could be accessed by class.variable name"
	"""note this comment will not included to class doc variable"""
	def __init__(self,movieTitle,movieStoryline,moviePoster,movieTrailer):
		#class constructor , firstargument of any method in class is self
		self.title = movieTitle  # this is how we define class variable
		self.storyline = movieStoryline
		self.poster_image_url = moviePoster
		self.trailer_youtube_url = movieTrailer

	def show_trailer(self):  # class method
		webbrowser.open(self.trailer_youtube_url)
# note: objects will be created in entertainment_center.py

