def fav_characters(*characters):
	print(f"Here are my favourite characters:")
	for character in characters:
		print(character.title())
fav_characters('rand', 'kaj', 'inej')

def build_profile(first, last, **details):
	print("My details are:")
	details['first_name'] = first.title()
	details['second_name'] = last.title()
	return details
user = build_profile('harikesh', 'kumar',
					 location = 'India',
					 study = 'Varanasi' )
print(user)

def made_car(name, company, **other_details):
	other_details['name'] = name.title()
	other_details['company'] = company.title()
	return made_car
cars = made_car('subaru', 'outback', color='blue', tow_package=True)
print(cars)