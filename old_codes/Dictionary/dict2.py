#6.5
rivers = {'nile' : 'egypt', 'ganges' : 'india', 'thames' : 'england'}
for river, country in rivers.items():
	print(f"The {river.title()} flows in {country.title()}.")
for river in rivers.keys():
	print(river.title())
for country in rivers.values():
	print(country.title())

#6.6
favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'inej': 'python',
	}
friends = ['jen', 'phil', 'kal', 'inej']
for friend in friends:
	print(friend.title())
	if friend in favorite_languages.keys():
		print(f"\tThanks {friend.title()}, for taking the pole!")
	else:
		print(f"\tHey {friend.title()}, you should take the pole.")
