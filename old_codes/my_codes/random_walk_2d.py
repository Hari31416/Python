import random
#creating a function
def random_walk(n):
	choices = [1, 2, 3, 4]
	x = 0
	y = 0
	for number in range (0,n):
		value = random.choice(choices)
		if value == 1:
			x += 1
		elif value == 3:
			x -= 1
		elif value == 2:
			y += 1
		elif value == 4:
			x -= 1
	return (x,y)
#making a list of coordinates after n steps
coordintes = []
for m in range(0,10):
	position = random_walk(1000)
	coordintes.append(position)
print(coordintes)
