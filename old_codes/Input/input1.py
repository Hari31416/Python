#7.1
demand = input("What type of car would you like to rent? ")
print(f"Let me see if I can find a {demand}")

#7.2
number = input("How many are in your group? ")
number = int(number)
if number > 8:
	print("You have to wait for a table!")
else:
	print("Your table is ready!")

#7.3
number = input("Give me a number and i'll tell you if it is a multiple of ten! ")
number = int(number)
if number % 10 == 0:
	print(f"\n{number} is a multiple of ten!")
else:
	print(f"\n{number} is NOT a multiple of ten!")