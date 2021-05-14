#9.7, 9.8
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
class Privilages:
	"""list for Privilages"""
	def __init__(self, privilages = ""):
		self.privilages = ['can post', 'can ban other users', 'can delete post']
	def show_privilages(self):
		print("An admin can have the following privilages:")
		for privilage in self.privilages:
			print(privilage)
		
class Admin(Users):
	"""Admins are also users"""
	def __init__(self, first_name, last_name, location, age):
		super().__init__(first_name, last_name, location, age)
		self.privilages = Privilages()
	
admin_1 = Admin('inej', 'ghaja', 'ketterdem', 19)
admin_1.privilages.show_privilages()

#9.9
class Car:
    """A simple attempt to represent a car."""
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")
    def update_odometer(self, mileage):
    
	    if mileage >= self.odometer_reading:
	        self.odometer_reading = mileage
	    else:
	        print("You can't roll back an odometer!")
    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles

class Battery:
    """A simple attempt to model a battery for an electric car."""
    def __init__(self, battery_size=75):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size
    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")
    def upgrade_battery(self):
    	if battery_size != 100:
    		battery_size = 100
class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""
    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery = Battery()
my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.upgrade_battery()

		