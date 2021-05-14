#9.1
class Restaurant:
	"""Describing a Restaurant"""
	def __init__(self, restaurant_name, cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
	def describe_restaurant(self):
		print(f"The name of the restaurant is {self.restaurant_name.title()}, with cuisine type {self.cuisine_type.title()}.")
	def open_restaurant(self):
		print("The restaurant is open!")
my_restaurant = Restaurant('dominoes', 'pizza')
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()
print(f"{my_restaurant.restaurant_name}")

#9.2
my_restaurant_1 = Restaurant('dominoes', 'pizza')
my_restaurant_2 = Restaurant('dominoes2', 'pizza')
my_restaurant_3 = Restaurant('dominoes3', 'pizza')
my_restaurant_1.describe_restaurant()
my_restaurant_2.describe_restaurant()
my_restaurant_3.describe_restaurant()

#9.3
class Users:
	"""describing for Users"""
	def __init__(self, first_name, last_name, location, age):
		self.first_name = first_name
		self.last_name = last_name
		self.location = location
		self.age = age
	def describe_user(self):
		details = {
				'fisrt_name' : self.first_name,
				'last_name' : self.last_name,
				'location' : self.location,
				'age' : self.age,
				}
		print(details)
	def greet_user(self):
		name = self.first_name.title() + ' ' + self.last_name.title()
		print(f"Hello, {name}!")

user_1 = Users('inej', 'ghaja', 'ketterdem', 19)
user_2 = Users('dalinar', 'kholin', 'roshar', 38)
user_1.describe_user()
user_1.greet_user()
user_2.describe_user()
user_2.greet_user()

