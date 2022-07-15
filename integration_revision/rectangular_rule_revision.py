from prettytable import PrettyTable
from numpy import *
import matplotlib.pyplot as plt

f = lambda x: x ** 2 + 2
start: int = 3
end: int = 5
shapes = 10
# create function curve
x_tup = linspace(start, end, shapes + 1, True, True)
# calculate point for shapes
x = x_tup[0].round(4)
y = array([f(p) for p in x]).round(4)
# create table
table = PrettyTable()
table.add_column('x', x)
table.add_column('f(x)', y)
print(table)
# calculate Area
ysum: float = 0
for i in range(len(y) - 1):
    ysum += y[i]
area = x_tup[1] * ysum

X = linspace(start, end, 1000, True).round(4)
Y = array([f(p) for p in X]).round(4)
# plot the curve line
plt.plot(X, Y, 'black')

# color under the curve
for i in range(len(X) - 1):
    xs = [X[i], X[i], X[i + 1], X[i + 1]]
    ys = [0, Y[i], Y[i + 1], 0]
    plt.fill(xs, ys, edgecolor='blue', alpha=.25)

for i in range(shapes):
    xs = [x[i], x[i], x[i + 1], x[i + 1]]
    ys = [0, y[i], y[i], 0]
    plt.fill(xs, ys, 'm', edgecolor='black', alpha=.55)

plt.title(f'Rectangular Rule, N  = {shapes}, Area = {round(area, 4)}')
plt.show()
