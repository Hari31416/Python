from random import choice


# define a random walk function with n as number of steps
def random_walk(n):
	choices = [1, -1]
	x = 0
	for number in range(0, n):
		value = choice(choices)
		x = x + value
	return x
# make a list for the final position after a number of trials
positions = []
for n in range (0,200):
	position = random_walk(1000)
	positions.append(position)
# make a list to note the number of times the particle is at a given position
positions_numbers = []
position1 = []
for m in range(min(positions), max(positions)):
	position_number = positions.count(m)
	value = (m, position_number)
	position1.append(value)
	positions_numbers.append(position_number)
from plotly.graph_objs import Bar, Layout
from plotly import offline
data = [Bar(x = positions, y = positions_numbers)]
x_axis_config = {'title': 'Position'}
y_axis_config = {'title': 'Frequency of position'}
my_layout = Layout(title='Results of rolling two D8 10000 times', 
	xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='graph.html')