from numpy import arange
from numpy import meshgrid
from numpy.random import seed
from numpy.random import rand
from matplotlib import pyplot


# objective function
def objective(x, y):
    return x ** 2.0 + y ** 2.0


r_min, r_max = -5.0, 5.0
xaxis = arange(r_min, r_max, 0.1)
yaxis = arange(r_min, r_max, 0.1)
x, y = meshgrid(xaxis, yaxis)
results = objective(x, y)
seed(1)
sample_x = r_min + rand(10) * (r_max - r_min)
sample_y = r_min + rand(10) * (r_max - r_min)
pyplot.contourf(x, y, results, levels=50, cmap='jet')
optima_x = [0.0, 0.0]
pyplot.plot([optima_x[0]], [optima_x[1]], '*', color='white')
pyplot.plot(sample_x, sample_y, 'o', color='black')
pyplot.show()