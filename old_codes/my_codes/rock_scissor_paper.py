import random
while True:
	values = ['rock', 'scissor', 'paper']
	value_3 = input("Press y to continue and n to exit: ")
	if value_3 == 'n':
		break
	value_1 = input("Choose among ('rock', 'scissor', 'paper'): ")
	value_2 = random.choice(values)
	print(f"Your choice is {value_1}.")
	print(f"Computer's choice is {value_2}.")
	if value_1 == value_2:
		print("Both your and Computer's choices are the same. It's a draw!")
	elif value_1 == 'rock' and value_2 == 'scissor':
		print("Rock blunts scissor. You win!")
	elif value_1 == "paper" and value_2 == 'scissor':
		print("Scissor cuts paper. You lost!")
	elif value_1 == "rock" and value_2 == "paper":
		print("Paper erodes rock. You lost!")
	elif value_1 == "paper" and value_2 == "rock":
		print("Paper erodes rock. You win!")
	elif value_1 == "scissor" and value_2 == "rock":
		print("Rock blunts scissor. You lost!")
	elif value_1 == "scissor" and value_2 == "paper":
		print("Scissor cuts paper. You win!")
	else:
		print(f"'{value_1}' is not related to the game. Please provide a valid choice.")
