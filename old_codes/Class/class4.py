#9.13
import random
from random import randint
class Dice():
	"""craeting an unbiased dice"""
	def __init__(self, sides = 6):
		self.sides = sides
	def roll_die(self):
		"""generating a random face"""
		value = randint(1, self.sides)
		return value
my_dice = Dice(10)
results = []
for n in range(0,100):
	result = my_dice.roll_die()
	results.append(result)
print(results)
for m in range(1,11):
	times = results.count(m)
	print(m, times)

#9.14
all_numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 'a', 'b', 'c', 'd')
lucky_numbers = []
print("People with following codes win the lottery:")
for n in range(1,5):
	lucky_number = random.choice(all_numbers)
	lucky_numbers.append(lucky_number)
	for string in lucky_numbers:
			print(string)


#9.15
all_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 'a', 'b', 'c', 'd']
my_tickets = [1, 7, 'a']
def lottery(ticket):
	while True:
		lucky_number = random.choice(all_numbers)
		print(lucky_number)
		if lucky_number != ticket:
			all_numbers.remove(lucky_number)
		elif lucky_number == ticket:
			break
lottery(4)
print(f"You won after {14 - len(all_numbers)} number of attempts.")
