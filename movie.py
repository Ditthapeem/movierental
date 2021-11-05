class Movie:
	"""
	A movie available for rent.
	"""
	
	def __init__(self, title, year, genre):
		# Initialize a new movie. 
		self.title = title
		self.year = year
		self.genre = genre
	
	def get_title(self):
		return self.title

	def get_year(self):
		return self.year

	def is_genre(self, string):
		if string in self.genre:
			return True
		else:
			return False

	def __str__(self):
		return self.title
