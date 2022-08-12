#3.1 Names
friends = ['rand', 'perrin', 'mat', 'kal', 'adolin', 'dalinar', 'kvothe']
print(friends)
print(friends[0].title())
print(friends[1])
print(friends[2])
print(friends[3])
print(friends[4])
#3.2 Greetings
print(f"Hello, {friends[0].title()}!")
print(f"Hello, {friends[1].title()}!")
print(f"Hello, {friends[2].title()}!")
print(f"Hello, {friends[3].title()}!")
#Using for loop
for friend in friends:
	print(f"Hello, {friend.title()}!")
#3.3 Your Own List
vehicles = ['car', 'bus', 'bike', 'train', 'tesla']
print(f"I would love to have a {vehicles[-1].title()}!")
print(f"I hate {vehicles[1]}.")

#Using element of the list as variable
chief_guest = friends[0]
print(chief_guest.title())

#Lenght of a list
print(f"I have {len(vehicles)} vehicles")

#adding two strings
string_1 = 'hello'
string_2 = ' there'
string_3 = string_1 + string_2
print(string_3.title())
