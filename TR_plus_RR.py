from numpy import round, linspace
import matplotlib.pyplot as plt
import numpy as np

f = lambda x: np.exp(x ** 2)
start = 0  # a
end = 1  # b
shapes = 5  # N
h = end - start / shapes


def rectangular_rule(startInterval, endInterval, noOfShapes):
    rr_h = (endInterval - startInterval) / noOfShapes
    x = linspace(startInterval, endInterval, noOfShapes)
    y = f(x)
    rr_sum = 0
    for i in y:
        rr_sum += i
    rr_sum = rr_h * rr_sum
    return rr_sum


def trapezoidal_rule(startInterval, endInterval, noOfShapes):
    tr_h = (endInterval - startInterval) / noOfShapes
    x = linspace(startInterval, endInterval, noOfShapes, True)
    y = f(x)
    tr_sum = 0
    for i in range(len(y)):
        if (i == 0) or (i == len(y) - 1):
            tr_sum = tr_sum + (y[i] * (tr_h / 2))
        else:
            tr_sum = tr_sum + (tr_h * y[i])
    return tr_sum


print(rectangular_rule(0, 1, 6))
print(trapezoidal_rule(0, 1, 6))
