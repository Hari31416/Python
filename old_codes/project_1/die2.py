from random import randint
from plotly.graph_objs import Bar, Layout
from plotly import offline
class Die:
	"""a simple dice"""
	def __init__(self, faces):
		self.faces = faces
	def rolling(self):
		return randint(1, self.faces)
die_1 = Die(25)
die_2 = Die(20)
results = []
for n in range(1, 10000):
	value = die_1.rolling() + die_2.rolling()
	results.append(value)
counts = []
for m in range(2, 46):
	count = results.count(m)
	counts.append(count)
print(counts)
x_values = list(range(2, 51))
data = [Bar(x = x_values, y = counts)]
x_axis_config = {'title': 'Result'}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title='Results of rolling two D8 10000 times', 
	xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d8d8.html')

		