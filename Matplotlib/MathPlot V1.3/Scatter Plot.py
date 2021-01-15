from numpy import arange
from matplotlib import pyplot


def objective(x):
    return x ** 2.0


r_min, r_max = -5.0, 5.0
inputs = arange(r_min, r_max, 0.1)
results = objective(inputs)
pyplot.scatter(inputs, results)
pyplot.show()
