import matplotlib.pyplot as plt
from numpy import *
import numpy as np
from prettytable import PrettyTable


def f(val):
    return ((3 / 7) * val) + (6 * val)
    # np.exp(val ** 2)  # other functions (4 * val + math.cos(4 * val)) / val change start and end to 1,4 respectively


# Calculating Points
start = 0
end = 6
shapes = 7
x_tup = linspace(start, end, shapes + 1, True, True)
x = x_tup[0].round(4)
y = [f(value) for value in x]
h = x_tup[1]
# Creating for console.
table = PrettyTable()
table.add_column('x', x)
table.add_column('y', y)

ysum = 0
for i in range(1, len(y) - 1):
    ysum += y[i]
area = round((x_tup[1] / 2) * (y[0] + 2 * ysum + y[-1]), 4)
print(table)
print('Area: ', area)
# Plotting Functions
X = linspace(start, end, 1000)
Y = [f(value) for value in X]
plt.plot(X, Y, 'black')
for i in range(len(X) - 1):
    xs = [X[i], X[i], X[i + 1], X[i + 1]]
    ys = [0, Y[i], Y[i + 1], 0]
    plt.fill(xs, ys, 'r', edgecolor='blue', alpha=.125)
for i in range(shapes):
    xs = [x[i], x[i], x[i + 1], x[i + 1]]
    ys = [0, y[i], y[i + 1], 0]
    plt.fill(xs, ys, 'm', edgecolor='magenta', alpha=.55)

plt.title(f'Trapezoidal Rule N={shapes}, Area={area}')
plt.show()
