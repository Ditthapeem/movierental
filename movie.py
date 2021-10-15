from enum import Enum


class PriceCode(Enum):
	new_release = {"price": lambda days: 3.0*days,
				   "frp": lambda days: days
		}
	regular = {"price": lambda days: 2 + ( 1.5 * (days - 2)) if days > 2 else 2,
				   "frp": lambda days: 1
		}
	childrens = {"price": lambda days:1.5 + (1.5 * (days - 3)) if days > 3 else 1.5,
				   "frp": lambda days: 1
		}

	def price(self, days: int) -> float:
		"""Returns the rental price for a given number of days."""
		pricing = self.value["price"]
		return pricing(days)

	def point(self, days: int) -> float:
		"""Returns the rental price for a given number of days."""
		points = self.value["frp"]
		return points(days)





class Movie:
	"""
	A movie available for rent.
	"""
	
	def __init__(self, title, price_code):
		# Initialize a new movie. 
		self.title = title
		self.price_code = price_code

	def get_price_code(self):
		# get the price code
		return self.price_code
	
	def get_title(self):
		return self.title

	def get_point(self, days):
		return self.price_code.point(days)

	def __str__(self):
		return self.title
