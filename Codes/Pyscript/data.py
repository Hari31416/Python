import numpy as np
import matplotlib.pyplot as plt


def plot_data(n):
    x = np.random.randn(n)
    y = np.random.randn(n)
    fig, ax = plt.subplots()
    ax.scatter(x, y, color="r")
    return fig

plot_data(1000)