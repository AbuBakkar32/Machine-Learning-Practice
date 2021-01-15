from numpy import arange
from matplotlib import pyplot


# objective function
def objective(x):
    return x ** 2.0


r_min, r_max = -5.0, 5.0
inputs = arange(r_min, r_max, 0.1)
results = objective(inputs)
pyplot.plot(inputs, results)
optima_x = 0.0
optima_y = objective(optima_x)
pyplot.plot([optima_x], [optima_y], 's', color='r')
pyplot.show()

print(optima_y)