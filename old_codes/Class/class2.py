#9.4
class Restaurant:
	"""Describing a Restaurant"""
	def __init__(self, restaurant_name, cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		self.number_served = 0
	def describe_restaurant(self):
		print(f"The name of the restaurant is {self.restaurant_name.title()}, with cuisine type {self.cuisine_type.title()}.")
	def open_restaurant(self):
		print("The restaurant is open!")
	def set_number_served(self, number):
		self.number_served = number
	def increment_number_served(self, serves):
		if serves >= 0:
			self.number_served += serves
			print(f"Number of serves is {self.number_served}.")
		else:
			print("Number of serves can not be negative!")

my_restaurant = Restaurant('dominoes', 'pizza')
print(my_restaurant.number_served)
my_restaurant.number_served = 10
print(my_restaurant.number_served)
my_restaurant.set_number_served(20)
print(my_restaurant.number_served)
my_restaurant.increment_number_served(12)

#9.5
class Users:
	"""describing for Users"""
	def __init__(self, first_name, last_name, location, age):
		self.first_name = first_name
		self.last_name = last_name
		self.location = location
		self.age = age
		self.login_attempts = 0
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
	def increment_login_attempts(self):
		self.login_attempts += 1
		print(f"Total number of attempted login is: {self.login_attempts}.")
	def reset_login_attempts(self):
		self.login_attempts = 0
user_1 = Users('inej', 'ghaja', 'ketterdem', 19)
user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.reset_login_attempts()
print(user_1.login_attempts)
user_1.increment_login_attempts()
user_1.increment_login_attempts()




