import numpy as np
from pulp import *
import matplotlib.pyplot as plt

prob = LpProblem('Lp_Lab_Task', LpMaximize)
x = LpVariable('a', 0)
y = LpVariable('b', 0)
prob += 4 * x + 6 * y
prob += -x + y <= 11, '1st_Constraint'
prob += x + y <= 27, '2nd_Constraint'
prob += 2 * x + 5 * y <= 90, '3rd Constraint'

prob.solve()
print('Status :', LpStatus[prob.status])

for v in prob.variables():
    print(v.name, ':', v.varValue)
print('Objective function Maximized Value :', value(prob.objective))

A = np.array([[-1, 1], [1, 1]])
b = np.array([11, 27])
x_s = np.linalg.solve(A, b)
print(x_s)

x1 = np.linspace(-15, 50)
plt.plot(x1, 11 + x1, label="-x+y <=11")
plt.plot(x1, 27 - x1, 'green', label="x+y <=27")
plt.plot(x1, (90 - 2 * x1) / 5, 'red', label="2x+5y <=90")
plt.ylim(-5, 30)
plt.grid()
plt.legend()
plt.fill([0, 27, 15, 5, 0], [0, 0, 12, 16, 11], 'Green')
plt.show()
