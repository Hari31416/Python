from random import choice
class RandomWalk:
	"""A class to generate random walks."""
	def __init__(self, num_points=10000):
		"""Initialize attributes of a walk."""
		self.num_points = num_points
		# All walks start at (0, 0).
		self.x_values = [0]
		self.y_values = [0]
	def fill_walk(self):
		"""Calculate all the points in the walk."""
		# Keep taking steps until the walk reaches the desired length.
		for number in range(0, self.num_points):
			# Decide which direction to go and how far to go in that direction.
			x_step = choice([1, -1])
			y_step = choice([1, -1])
			# Calculate the new position.
			x = self.x_values[-1] + x_step
			y = self.y_values[-1] + y_step
			self.x_values.append(x)
			self.y_values.append(y)
import matplotlib.pyplot as plt
#calling the function
rw = RandomWalk()
rw.fill_walk()
#last point
print(rw.x_values[-1], rw.y_values[-1])
#maximum displacement
plt.style.use('seaborn')
fig, ax = plt.subplots()
#creating a variable for coloring the plot
numbers = range(0, 10001)
#plotting the points
ax.scatter(rw.x_values, rw.y_values, c=numbers, cmap=plt.cm.Reds, s=10)
#Origin
ax.scatter(0, 0, c='green', edgecolors='none', s=100)
#The final position
ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none',
	s=100)
plt.show()