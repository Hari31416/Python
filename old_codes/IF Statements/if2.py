#5.8 9
usernames = ['admin', 'rand', 'kal', 'shallan']
if usernames:
	for user in usernames:
		if user == 'admin':
			print('Hello ADMIN!')
		else:
			print(f"Hello {user.title()}!")
else:
	print("We need more users.")

#5.10
current_users = ['rand', 'kal', 'shallan', 'inej', 'zoya']
new_users = ['denna', 'Kal', 'rand', 'shallan', 'kaj']
for users in new_users:
	if users.lower() in current_users:
		print(f"{users} is no longer avalaible!")
	else:
		print(f"You can use the name {users}!")

#copying a list1
current_users = ['Rand', 'kAl', 'shallaN', 'INEJ', 'zoya']
current_users_lower = []
print(current_users)
for users in current_users:
	current_users_lower.append(users.lower())
print(current_users_lower)

#copying a list2
current_users = ['Rand', 'kAl', 'shallaN', 'INEJ', 'zoya']
current_users_lower = [user.upper() for user in current_users]
print(current_users_lower)

#5.11
numbers = [number for number in range(1, 20)]
for number in numbers:
	if number == 1:
		print("1st")
	elif number == 2:
		print("2nd")
	elif number == 3:
		print("3rd")
	else:
		print(f"{number}th")
