#numbers
numbers = [value for value in range (1,50)]
print(numbers)
odd_numbers = numbers[0:50:2]
print(odd_numbers)

#players
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("Here are the first three players on my team:")
for player in players[:3]:
	print(player.title())
	
#friends
friends = ['rand', 'perrin', 'mat', 'kal', 'adolin', 'dalinar', 'kvothe']
print(friends[0:3])
print(friends[2:5])
print(friends[4:7])
print(friends[-3:])
print(friends[:-3])

friends_boys = ['rand', 'perrin', 'mat', 'kal', 'adolin', 'dalinar', 'kvothe']
friends_girls = ['vin', 'shallan', 'denna', 'vivena']
friends_all = friends_boys[:] + friends_girls[:]
friends_boys.append('kaz')
friends_girls.append('inej')
friends_all.append('nikolai')
print(friends_boys)
print(friends_girls)
print(friends_all)
print(len(friends_all))
friends_all.sort()
for friend in friends_all:
	print(f"Hello {friend.title()}!")
