try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")

#10.6 10.7
while True:
	print("Press q anytime to close.")
	num_1 = input("Type the first number: ")
	num_2 = input("Type the second number: ")
	if num_1 == 'q':
		break
	elif num_2 == 'q':
		break
	else:
		try:
			number_1 = int(num_1)
			number_2 = int(num_2)
			print(number_1 + number_2)
		except ValueError:
			print(f"You can not add {num_1} with {num_2}!")
			

