#8.1
def hello():
	print("Hello, I'm reading about functions.")
hello()

#8.2
def favorite_book(title):
	"""My favourite book"""
	print(f"One of my favourite book is {title.title()}!")
favorite_book("six of crows")

#8.3
def make_shirt(text, size):
	print(f"Make a T-Shirt of size {size} with the text '{text.title()}'.")
make_shirt("all thoose wander are not lost", "L")
make_shirt("perfect", "XL")

#8.4
def make_shirt(text, size = "L"):
	print(f"Make a T-Shirt of size {size} with the text '{text.title()}'.")
make_shirt("all thoose wander are not lost")
make_shirt("perfect", "XL")

#8.5
def describe_city(city_name, country = "india"):
	print(f"{city_name.title()} is situated in {country.title()}.")
describe_city('agra')
describe_city('shimla')
describe_city('new york', 'america')