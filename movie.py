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


class MovieCatalog:

	def __init__(self):
		self.movie_data = []
		file = open("movies.csv", "r")
		for _ in file:
			new_movie = file.readline().strip("\n").split(",")
			movie_data = {'id': new_movie[0], 'title': new_movie[1], 'year': new_movie[2], 'genre': new_movie[3]}
			self.movie_data.append(movie_data)

	def get_movie(self, title):
		# Search for title
		for movie_data in self.movie_data:
			if title == movie_data["title"]:
				return Movie(movie_data["title"], movie_data["year"], movie_data["genre"])
		# If the title doesn't match append in data
		for id in self.movie_data:
			new_id = id['id']
		self.movie_data.append({'id': int(new_id)+1, 'title': title, 'year': "Unknown", 'genre': "Unknown"})
		return Movie(title, "Unknown", "Unknown")

# 	def debug(self):
# 		return self.movie_data
#
#
# movie = MovieCatalog()
# print(movie.get_movie("Mulan").year)
