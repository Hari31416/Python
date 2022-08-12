import random
def roll(faces):
	result = random.randint(1, faces)
	return result
results = []
for n in range(1,960):
	die = roll(8)
	results.append(die)
counts = []
for m in range(1, 9):
	count = results.count(m)
	counts.append(count)
print(counts)
from plotly.graph_objs import Bar, Layout
from plotly import offline
x_values = list(range(1, 9))
data = [Bar(x = x_values, y = counts)]
x_axis_config = {'title': 'Result'}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title='Results of rolling one D6 1000 times', 
	xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d6.html')