from numpy import arange
from numpy.random import seed
from numpy.random import rand
from matplotlib import pyplot


# objective function
def objective(x):
    return x ** 2.0


r_min, r_max = -5.0, 5.0
inputs = arange(r_min, r_max, 0.1)
results = objective(inputs)
seed(1)
sample = r_min + rand(10) * (r_max - r_min)
sample_eval = objective(sample)
pyplot.plot(inputs, results)
optima_x = 0.0
pyplot.axvline(x=optima_x, ls='--', color='red')
pyplot.plot(sample, sample_eval, 'o', color='black')
pyplot.show()