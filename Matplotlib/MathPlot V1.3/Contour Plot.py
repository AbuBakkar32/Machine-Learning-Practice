from numpy import arange
from numpy import meshgrid
from matplotlib import pyplot


# objective function
def objective(x, y):
    return x ** 2.0 + y ** 2.0


r_min, r_max = -5.0, 5.0
xaxis = arange(r_min, r_max, 0.1)
yaxis = arange(r_min, r_max, 0.1)
x, y = meshgrid(xaxis, yaxis)
results = objective(x, y)
pyplot.contour(x, y, results, 50, alpha=1.0, cmap='jet')
pyplot.show()
