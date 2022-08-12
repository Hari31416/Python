current_number = 1
while current_number <= 5:
	print(current_number)
	current_number += 1

#7.4
prompt = "Which type of pizza toppings would you like?"
prompt += "\nPress 'quit' to exit. "
message = input(prompt)
if message != 'quit':
	print(f"We are adding {message} to you pizza!")
else:
	print("Thank You!")

#7.5
prompt = "What is your age? "
age = input(prompt)
age = int(age)
if age <= 3:
	print("Your ticket is free!")
elif age <= 12:
	print("Your ticket fee is $10!")
elif age > 12:
	print("Your ticket is $15!")

#flag
value = input("Give me a number: ")
value = int(value)
active = True
while active:
	value += 2
	if value > 44:
		active = False
		print(value)

