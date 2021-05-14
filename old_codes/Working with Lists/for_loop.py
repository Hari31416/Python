
#exercise
friends = ['rand', 'perrin', 'mat', 'kal', 'adolin', 'dalinar', 'kvothe']
for friend in friends:
	print(f"Hello, {friend.title()}!")


guests = ['rand', 'perrin', 'mat', 'nightblood']
guests.insert(0, 'shallan')
guests.insert(3, 'vin')
guests.append('denna')
print(guests)
print(len(guests))
for guest in guests:
	print(f"Hello, {guest.title()}! Would you like to have dinner?")
print(len(guests))



