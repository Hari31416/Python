filename = 'e.txt'
with open(filename) as file_object:
	e = ""
	for line in file_object:
		e += line.strip()

def digits(n):
	n = int(n)
	e_ = []
	e_count = []
	for value in e[2:n]:
		e_.append(value)
	for m in range(0, 10):
		m = str(m)
		e_count.append(e_.count(m))
	from plotly.graph_objs import Bar, Layout
	from plotly import offline
	x_values = list(range(0, 10))
	data = [Bar(x = x_values, y = e_count)]
	x_axis_config = {'title': 'Digits'}
	y_axis_config = {'title': 'Frequency of Digits'}
	my_layout = Layout(title='The frequency of digits in e', 
		xaxis=x_axis_config, yaxis=y_axis_config)
	offline.plot({'data': data, 'layout': my_layout}, filename='e.html')
digits(1000000)
