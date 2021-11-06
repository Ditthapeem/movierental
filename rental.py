import logging
from enum import Enum
from datetime import datetime

class Rental:
	"""
	A rental of a movie by customer.
	From Fowler's refactoring example.

	A realistic Rental would have fields for the dates
	that the movie was rented and returned, from which the
	rental period is calculated.
	But for simplicity of the example only a days_rented
	field is used.
	"""
	
	def __init__(self, movie, days_rented, price_code):
		"""Initialize a new movie rental object for
		   a movie with known rental period (daysRented).
		"""
		if not isinstance(price_code, PriceCode):
			raise f"Movie {self.get_movie()} has unrecognized priceCode"
		self.movie = movie
		self.days_rented = days_rented
		self.price_code = price_code

	def get_price_code(self):
		return self.price_code

	def get_movie(self):
		return self.movie

	def get_days_rented(self):
		return self.days_rented

	def get_charge(self):
		return self.price_code.price(self.days_rented)
		# amount = 0
		# if self.get_movie().get_price_code() == PriceCode.regular:
		# 	# Two days for $2, additional days 1.50 each.
		# 	amount = 2.0
		# 	if self.get_days_rented() > 2:
		# 		amount += 1.5 * (self.get_days_rented() - 2)
		# elif self.get_movie().get_price_code() == PriceCode.childrens:
		# 	# Three days for $1.50, additional days 1.50 each.
		# 	amount = 1.5
		# 	if self.get_days_rented() > 3:
		# 		amount += 1.5 * (self.get_days_rented() - 3)
		# elif self.get_movie().get_price_code() == PriceCode.new_release:
		# 	# Straight per day charge
		# 	amount = 3 * self.get_days_rented()
		# else:
		# 	log = logging.getLogger()
		# 	log.error(f"Movie {self.get_movie()} has unrecognized priceCode {self.get_movie().get_price_code()}")
		# return amount

	def get_renter_point(self):
		# award renter points
		renter_point = 0
		if self.get_price_code() == PriceCode.new_release:
			renter_point += self.get_days_rented()
		else:
			renter_point += 1
		return renter_point


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

	def for_movie(movie):
		if datetime.today().year == movie.year:
			return PriceCode.new_release
		elif movie.is_genre("Children"):
			return PriceCode.childrens
		else:
			return PriceCode.regular
