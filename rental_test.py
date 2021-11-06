import unittest
from customer import Customer
from rental import Rental, PriceCode
from movie import Movie, MovieCatalog


class RentalTest(unittest.TestCase):
	
	def setUp(self):
		self.catalog = MovieCatalog()
		self.new_movie = self.catalog.get_movie("Mulan")
		self.regular_movie = self.catalog.get_movie("CitizenFour")
		self.childrens_movie = self.catalog.get_movie("Frozen")

	def test_movie_attributes(self):
		"""trivial test to catch refactoring errors or change in API of Movie"""
		m = self.catalog.get_movie("CitizenFour")
		self.rental = Rental(m, 5, PriceCode.for_movie(m))
		self.assertEqual("CitizenFour", m.get_title())
		self.assertEqual(PriceCode.regular, self.rental.get_price_code())

	def test_rental_price(self):
		rental = Rental(self.new_movie, 1, PriceCode.for_movie(self.new_movie))
		self.assertEqual(rental.get_charge(), 2.0)
		rental = Rental(self.new_movie, 5, PriceCode.for_movie(self.new_movie))
		self.assertEqual(rental.get_charge(), 6.5)
		rental = Rental(self.new_movie, 4, PriceCode.for_movie(self.new_movie))
		self.assertEqual(rental.get_charge(), 5.0)

	def test_rental_points(self):
		rental = Rental(self.new_movie, 4, PriceCode.for_movie(self.new_movie))
		self.assertEqual(rental.get_renter_point(), 1.0)
		rental = Rental(self.regular_movie, 3, PriceCode.for_movie(self.regular_movie))
		self.assertEqual(rental.get_renter_point(), 1)
		rental = Rental(self.childrens_movie, 3, PriceCode.for_movie(self.childrens_movie))
		self.assertEqual(rental.get_renter_point(), 1)

