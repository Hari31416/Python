filename = 'pie.txt'
with open(filename) as file_object:
	pie = ""
	for line in file_object:
		pie += line.strip()

def digits(n):
	n = int(n)
	pie_ = []
	pie_count = []
	for value in pie[2:n]:
		pie_.append(value)
	for m in range(0, 10):
		m = str(m)
		pie_count.append(pie_.count(m))
	from plotly.graph_objs import Bar, Layout
	from plotly import offline
	x_values = list(range(0, 10))
	data = [Bar(x = x_values, y = pie_count)]
	x_axis_config = {'title': 'Digits'}
	y_axis_config = {'title': 'Frequency of Digits'}
	my_layout = Layout(title='The frequency of digits in pie', 
		xaxis=x_axis_config, yaxis=y_axis_config)
	offline.plot({'data': data, 'layout': my_layout}, filename='pie.html')
digits(10000000)
