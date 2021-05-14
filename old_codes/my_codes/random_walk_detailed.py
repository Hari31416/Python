from random import choice
class RandomWalk():
	"""a simple model of random walk problem"""
	def __init__(self, steps):
		self.steps = steps
		"""setting initial positions"""
		self.x_o = [0]
		self.y_o = [0]
	def multiple_step(self):
		"""running single_step a number of times"""
		for n in range(1, self.steps):
			x_value = choice([1, -1])
			y_value = choice([1, -1])
			self.x_o.append(self.x_o[-1] + x_value)
			self.y_o.append(self.y_o[-1] + y_value)
rw = RandomWalk(10000)
rw.multiple_step()
import matplotlib.pyplot as plt
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(rw.x_o, rw.y_o)
plt.show()
