# Demonstrate the movie rental code.
# Create a customer with some movies and print a statement.

from movie import Movie
from rental import Rental, PriceCode
from customer import Customer

def make_movies():
    movies = [
        Movie("The Irishman", PriceCode.new_release),
        Movie("CitizenFour", PriceCode.regular),
        Movie("Frozen", PriceCode.childrens),
        Movie("El Camino", PriceCode.new_release),
        Movie("Particle Fever", PriceCode.regular)
    ]
    return movies


if __name__ == '__main__':
    # Create a customer with some rentals
    customer = Customer("Edward Snowden")
    days = 1
    for movie in make_movies():
        customer.add_rental(Rental(movie, days))
        days += 1
    print(customer.statement())
