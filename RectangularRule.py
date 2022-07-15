import matplotlib.pyplot as plt
from numpy import linspace, array
from prettytable import PrettyTable

f = lambda e: e ** 2 + 2

start = 3
end = 5
shapes = 7
# Console Calculations
x_tup = linspace(start, end, shapes + 1, True, True)
x = x_tup[0].round(4)
y = array([f(e) for e in x]).round(4)
table = PrettyTable()
table.add_column('x', x)
table.add_column('f(x)', y)

print(table)
# calculate Area
ysum = 0
for i in range(len(y) - 1):
    ysum += y[i]
area = x_tup[1] * ysum
print('Area under the curve: ', round(area, 4))

# Plotting Functions
X = linspace(start, end, 1000)
Y = f(X)
plt.plot(X, Y, 'black')

# color fill under the curve
for i in range(len(X) - 1):
    xs = [X[i], X[i], X[i + 1], X[i + 1]]
    ys = [0, Y[i], Y[i + 1], 0]
    plt.fill(xs, ys, edgecolor='blue', alpha=.25)
# color fill in the rectangular shapes
for i in range(shapes):
    xs = [x[i], x[i], x[i + 1], x[i + 1]]
    ys = [0, y[i], y[i], 0]
    plt.fill(xs, ys, 'm', edgecolor='black', alpha=.55)

plt.title(f'Rectangular Rule,N={shapes}, Area={round(area, 4)}')
plt.show()
