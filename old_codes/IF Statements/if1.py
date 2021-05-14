#5.3
alien_color = ['green', 'yellow', 'red']
if 'green' in alien_color:
	print('You just earned 5 points!')
if 'blue' in alien_color:
	print('You just earned 5 points!')

#5.4
alien_color = ['green', 'yellow', 'red']
if 'yellow' in alien_color:
	print('You just earned 10 points!')
elif 'green' in alien_color:
	print('You just earned 5 points!')
elif 'red' in alien_color:
	print('You just earned 15 points!')	

#5.6
age = 70
if age < 2:
	stage = 'baby'
elif age < 4:
	stage = 'toddler'
elif age < 13:
	stage = 'child'
elif age < 20:
	stage = 'teenager'
elif age < 65:
	stage = 'adult'
else:
	stage = 'elder'
print(f"You are {stage}!")

#5.7
favourite_fruits = ['apple', 'mango', 'banana', 'chikoo']
if 'apple' in favourite_fruits:
	print('I love apple!')
if 'mango' in favourite_fruits:
	print('I love mango!')
if 'banana' in favourite_fruits:
	print('I love banana!')
if 'chikoo' in favourite_fruits:
	print('I do not like chikoo!')
	
