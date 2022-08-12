#15.1
import math
import matplotlib.pyplot as plt
input_values = [x/100 for x in range(-2000, 2001)]
output_1 = [math.sin(x) for x in input_values]
output_2 = [math.cos(x) for x in input_values]
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(input_values, output_1, linewidth = 1, c= 'green')
ax.plot(input_values, output_2, linewidth = 1, c= 'red')
#setting title and axes
ax.set_title('sine of x(green) and cos of x(red)', fontsize = 14)
ax.set_xlabel('x', fontsize = 14)
ax.set_ylabel('sin(x) & cos(x)', fontsize = 14)
# Set size of tick labels.
ax.tick_params(axis='both', labelsize=14)
plt.show()


